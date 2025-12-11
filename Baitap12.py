#Bài tập 6: Tìm tổng các chữ số của một số
#Viết chương trình:
#Nhập vào số nguyên 3 chữ số
#Tính tổng các chữ số
#Ví dụ:  123 → 1 + 2 + 3 = 6
a = int(input("Nhập dữ liệu số nguyên 3 chữ số:"))
hangTram = a // 100
hangChuc = (a // 10) % 10
hangDonvi = a % 10
Tong = hangTram + hangChuc + hangDonvi
print(Tong)