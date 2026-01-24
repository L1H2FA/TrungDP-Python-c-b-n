import tkinter as tk
root = tk.Tk()
root.title("First_Program")
root.geometry("800x500")
def dang_nhap():
    ten = entry_taikhoan.get()
    label_hienthi.config(
        text = f"Bạn đã nhập tên đăng nhập là: {ten}"
    )
#Hiện tên đã đăng nhập
label_hienthi = tk.Label(root, text ="", font=("Arial",12))
label_hienthi.pack(pady=10)
#Hiện thị ô nhập tên đăng nhập
label_input = tk.Label(root, text ="Tên đăng nhập", font =("Arial", 12))
label_input.pack(pady=5)
#Hiển thị vị trí ô nhập tài khoản
entry_taikhoan = tk.Entry(root, font =("Arial",12), width = 30)
entry_taikhoan.pack(pady=5)
#Nút đăng nhập
btn_dangnhap = tk.Button(
root,
text="Đăng Nhập",
font=("Arial",12),
command=dang_nhap
)
btn_dangnhap.pack(pady=10)
root.mainloop()