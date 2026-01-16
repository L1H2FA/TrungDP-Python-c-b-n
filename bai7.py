#Bài tập 7(*): Bài tập lớn
#Viết chương trình quản lý bạn bè trên facebook 
#Chương trình cho phép người dùng lưu trữ 
#tên bạn bè và thực hiện các chức năng sau: 
#1.	Hiển thị menu tùy chọn
# Chương trình quản lý bạn bè facebook
# Nhập Phím 1 để hiện thị danh sách bạn bè
# Nhập phím 2 để thêm mới bạn bè
# Nhập Phím 3 để xóa bạn bè
# Nhập phím 4 để sửa tên bạn bè
# Nhập phím 5 để thoát chương trình
#2.	Hiển thị danh sách bạn bè : Hiển thị danh sách tất cả các bạn bè đang lưu trữ
#3.	Cho phép thêm mới bạn bè: Thực hiện thêm mới bạn bè vào danh sách
#4.	Cho phép chỉnh sửa tên bạn bè: Cho phép chỉnh sửa tên bạn bè
#5.	Cho phép xóa bạn bè: cho phép xóa bạn bè ra khỏi danh sách
# Quan ly ban be Facebook (dung List)
ds = []  # list luu ten ban be

while True:
    print("\n===== MENU QUAN LY BAN BE =====")
    print("1. Hien thi danh sach ban be")
    print("2. Them moi ban be")
    print("3. Xoa ban be")
    print("4. Sua ten ban be")
    print("5. Thoat")
    
    chon = input("Nhap lua chon (1-5): ")

    if chon == "1":
        if len(ds) == 0:
            print("Danh sach dang rong!")
        else:
            print("\n--- Danh sach ban be ---")
            for i in range(len(ds)):
                print(i + 1, ".", ds[i])

    elif chon == "2":
        ten = input("Nhap ten ban be muon them: ")
        ds.append(ten)
        print("Da them:", ten)

    elif chon == "3":
        if len(ds) == 0:
            print("Danh sach rong, khong xoa duoc!")
        else:
            print("\n--- Danh sach ban be ---")
            for i in range(len(ds)):
                print(i + 1, ".", ds[i])

            vt = int(input("Nhap so thu tu ban be muon xoa: "))
            if vt < 1 or vt > len(ds):
                print("So thu tu khong hop le!")
            else:
                print("Da xoa:", ds[vt - 1])
                del ds[vt - 1]

    elif chon == "4":
        if len(ds) == 0:
            print("Danh sach rong, khong sua duoc!")
        else:
            print("\n--- Danh sach ban be ---")
            for i in range(len(ds)):
                print(i + 1, ".", ds[i])

            vt = int(input("Nhap so thu tu ban be muon sua: "))
            if vt < 1 or vt > len(ds):
                print("So thu tu khong hop le!")
            else:
                ten_moi = input("Nhap ten moi: ")
                ds[vt - 1] = ten_moi
                print("Da sua thanh:", ten_moi)

    elif chon == "5":
        print("Thoat chuong trinh!")
        break

    else:
        print("Lua chon khong hop le, vui long nhap 1-5!")

