#Bài tập 2: 
#Sử dụng Tkinter để xây dựng ứng dụng cho phép người dùng điền vào form các thông tin như họ và tên, số điện thoại, email, ngày tháng năm sinh để đăng ký nhận khuyến mãi.
#Sau khi người dùng nhập đầy đủ thông tin và nhấn nút submit sẽ lưu thông tin vào file khuyenmai.csv 
#Giao diện mẫu:
import os
import csv
import re
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import date

CSV_FILE = "khuyenmai.csv"

EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")


def ensure_csv_header(path: str):
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["ho_ten", "so_dien_thoai", "email", "ngay_sinh"])


def append_row(path: str, row: list[str]):
    with open(path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(row)


def only_digits(s: str) -> bool:
    return s.isdigit()


class PromoFormApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        root.title("Form Đăng ký Khuyến mãi")
        root.geometry("720x520")
        root.minsize(640, 480)

        # ====== Theme / Style (dark) ======
        self.bg = "#111111"
        self.card = "#1a1a1a"
        self.fg = "#f2f2f2"
        self.muted = "#cfcfcf"

        root.configure(bg=self.bg)

        style = ttk.Style()
        # 'clam' dễ tùy biến màu hơn trên nhiều OS
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure("TFrame", background=self.bg)
        style.configure("Card.TFrame", background=self.card)
        style.configure("TLabel", background=self.card, foreground=self.fg, font=("Segoe UI", 11))
        style.configure("Title.TLabel", background=self.card, foreground=self.fg, font=("Segoe UI", 16, "bold"))
        style.configure("Header.TLabel", background=self.card, foreground=self.fg, font=("Segoe UI", 12, "bold"))

        style.configure("TEntry", fieldbackground="#ffffff")
        style.configure("TCombobox", fieldbackground="#ffffff")
        style.map(
            "TCombobox",
            fieldbackground=[("readonly", "#ffffff")],
            foreground=[("readonly", "#000000")],
        )

        style.configure("Primary.TButton", font=("Segoe UI", 11, "bold"), padding=(12, 10))

        # ====== Layout container ======
        outer = ttk.Frame(root, padding=18)
        outer.pack(fill="both", expand=True)

        card = ttk.Frame(outer, style="Card.TFrame", padding=(26, 22))
        card.pack(fill="both", expand=True)

        # ====== Title ======
        title = ttk.Label(card, text="ĐĂNG KÝ NHẬN KHUYẾN MÃI", style="Title.TLabel", anchor="center")
        title.pack(pady=(8, 26))

        # ====== Form area ======
        form = ttk.Frame(card, style="Card.TFrame")
        form.pack(fill="x")

        # Grid config
        form.columnconfigure(0, weight=0)
        form.columnconfigure(1, weight=1)

        # Inputs
        self.var_name = tk.StringVar()
        self.var_phone = tk.StringVar()
        self.var_email = tk.StringVar()

        self._row_entry(form, 0, "Họ và tên:", self.var_name)
        self._row_entry(form, 1, "Số điện thoại:", self.var_phone)
        self._row_entry(form, 2, "Email:", self.var_email)

        # DOB row
        lbl_dob = ttk.Label(form, text="Ngày sinh:")
        lbl_dob.grid(row=3, column=0, sticky="w", padx=(0, 14), pady=10)

        dob_wrap = ttk.Frame(form, style="Card.TFrame")
        dob_wrap.grid(row=3, column=1, sticky="ew", pady=10)
        dob_wrap.columnconfigure(0, weight=1)
        dob_wrap.columnconfigure(1, weight=1)
        dob_wrap.columnconfigure(2, weight=1)

        today = date.today()
        years = list(range(today.year, 1900, -1))
        months = list(range(1, 13))
        days = list(range(1, 32))

        self.var_day = tk.StringVar(value="Ngày")
        self.var_month = tk.StringVar(value="Tháng")
        self.var_year = tk.StringVar(value="Năm")

        self.cb_day = ttk.Combobox(dob_wrap, values=days, textvariable=self.var_day, state="readonly", width=8)
        self.cb_month = ttk.Combobox(dob_wrap, values=months, textvariable=self.var_month, state="readonly", width=8)
        self.cb_year = ttk.Combobox(dob_wrap, values=years, textvariable=self.var_year, state="readonly", width=10)

        self.cb_day.grid(row=0, column=0, sticky="w")
        self.cb_month.grid(row=0, column=1, sticky="w", padx=10)
        self.cb_year.grid(row=0, column=2, sticky="w")

        # Hint / error label (optional)
        self.hint = tk.Label(card, text="", bg=self.card, fg="#ffb3b3", font=("Segoe UI", 10))
        self.hint.pack(pady=(10, 0))

        # Submit button
        btn = ttk.Button(card, text="Đăng ký nhận khuyến mãi", style="Primary.TButton", command=self.on_submit)
        btn.pack(pady=(24, 10))

    def _row_entry(self, parent: ttk.Frame, row: int, label: str, var: tk.StringVar):
        lbl = ttk.Label(parent, text=label)
        lbl.grid(row=row, column=0, sticky="w", padx=(0, 14), pady=10)

        ent = ttk.Entry(parent, textvariable=var)
        ent.grid(row=row, column=1, sticky="ew", pady=10)

    def set_hint(self, text: str):
        self.hint.config(text=text)

    def validate(self):
        name = self.var_name.get().strip()
        phone = self.var_phone.get().strip()
        email = self.var_email.get().strip()

        # DOB values
        day = self.var_day.get()
        month = self.var_month.get()
        year = self.var_year.get()

        if not name or not phone or not email:
            return False, "Vui lòng nhập đầy đủ Họ và tên / Số điện thoại / Email."

        if not only_digits(phone) or len(phone) < 9 or len(phone) > 12:
            return False, "Số điện thoại chỉ gồm chữ số và độ dài khoảng 9–12 ký tự."

        if not EMAIL_RE.match(email):
            return False, "Email không hợp lệ. Ví dụ: ten@gmail.com"

        if day in ("Ngày", "") or month in ("Tháng", "") or year in ("Năm", ""):
            return False, "Vui lòng chọn đầy đủ Ngày / Tháng / Năm sinh."

        # Check date validity (e.g., 31/02)
        try:
            dob = date(int(year), int(month), int(day))
        except ValueError:
            return False, "Ngày sinh không hợp lệ (ví dụ: 31/02)."

        # Reasonable age check (optional)
        if dob > date.today():
            return False, "Ngày sinh không thể ở tương lai."

        return True, ""

    def on_submit(self):
        ok, msg = self.validate()
        if not ok:
            self.set_hint(msg)
            return

        self.set_hint("")

        name = self.var_name.get().strip()
        phone = self.var_phone.get().strip()
        email = self.var_email.get().strip()
        dob_str = f"{int(self.var_day.get()):02d}/{int(self.var_month.get()):02d}/{self.var_year.get()}"

        try:
            ensure_csv_header(CSV_FILE)
            append_row(CSV_FILE, [name, phone, email, dob_str])
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể lưu file CSV:\n{e}")
            return

        messagebox.showinfo("Thành công", "Đăng ký thành công! Dữ liệu đã được lưu vào khuyenmai.csv")

        # Clear form
        self.var_name.set("")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_day.set("Ngày")
        self.var_month.set("Tháng")
        self.var_year.set("Năm")


def main():
    root = tk.Tk()
    app = PromoFormApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
