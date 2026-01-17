"""
Bài tập 2(*): Bài tập lớn
Chương trình quản lý quốc gia và thủ đô.
ví dụ: {‘Viet Nam’:’Ha Noi’, ‘Indonesia’:’Jakarta’, USA:’Washington’}
Chương trình cho phép người dùng có các tùy chọn thêm mới quốc gia và thủ đô, sửa tên thủ đô, xóa quốc gia và thủ đô, tìm kiếm thủ đô khi người dùng nhập vào quốc gia, hiển thị danh sách các quốc gia và thủ đô có trong chương trình
Sử dụng ngôn ngữ Python để xây dựng ứng dụng với các chức năng sau:
1.	Hiển thị menu tùy chọn
2.	Hiển thị danh sách các quốc gia và thủ đô có trong chương trình
3.	Cho phép thêm mới quốc gia và thủ đô
4.	Cho phép chỉnh sửa tên thủ đô
5.	Cho phép xóa quốc gia và thủ đô
6.	Cho phép tìm kiếm thủ đô khi người dùng nhập tên quốc gia
7.	Thoát chương trình
"""
DN_TD ={
    "Viet Nam": "Ha Noi",
    "Indonesia": "Jakarta",
    "USA": "Washington"
}
def hien_thi_menu():
    print("\n Quản lý quốc gia và thủ đô")
    print("1.Hiện thị menu")
    print("2. Hiện thị danh sách các quốc gia và thủ đô")
    print("3. Thêm quốc gia và thủ đô")
    print("4 Chỉnh sửa tên thủ đô")
    print("5. Xóa quốc gia và thủ đô")
    print("6.Tìm kiếm thủ đô theo tên quốc gia")
    print("7. Thoát chương trình")
def hien_thi_danh_sach():
    if len(DN_TD) == 0:
        print("Danh sách trống")
    else:
        print("\n DANH SÁCH QUỐC QIA VÀ THỦ ĐÔ ")
        for QG, TD in DN_TD.items():
            print(f"{QG} : {TD}")
def them_moi():
    QG = input(" Nhập tên quốc gia: ").strip()
    TD = input(" Nhập tên thủ đô: ").strip()
    if QG == "" or TD =="":
        print(" Không được để trống")
        return
    if QG in DN_TD:
        print("Quốc gia đã tồn tại")
    else:
        DN_TD[QG] = TD
        print(" Đã thêm thành công!")
def sua_thu_do():
    QG = input(" Nhập tên quốc gia cần sửa thủ đô: ").strip()
    if QG in DN_TD:
        TD_moi = input("Nhập tên thủ đô mới: ").strip()
        if TD_moi == "":
            print(" Thủ đô không được để trống!")
            return
        DN_TD[QG] = TD_moi
        print(" Cập nhật thành công")
    else:
        print(" Không tìm thấy quốc gia này!")


def xoa():
    QG = input("Nhập tên quốc gia cần xóa: ").strip()

    if QG in DN_TD:
        del DN_TD[QG]
        print("Xóa thành công!")
    else:
        print("Không tìm thấy quốc gia này!")

def tim_kiem():
    QG = input("Nhập tên quốc gia để tìm thủ đô: ").strip()

    if QG in DN_TD:
        print(f"Thủ đô của {QG} là: {DN_TD[QG]}")
    else:
        print("Không tìm thấy quốc gia này!")

# Chương trình chính
hien_thi_menu()
while True:
    chon = input("\nChọn chức năng (1-7): ").strip()

    if chon == "1":
        hien_thi_menu()
    elif chon == "2":
        hien_thi_danh_sach()
    elif chon == "3":
        them_moi()
    elif chon == "4":
        sua_thu_do()
    elif chon == "5":
        xoa()
    elif chon == "6":
        tim_kiem()
    elif chon == "7":
        print("Đã thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ! Vui lòng chọn lại.")
