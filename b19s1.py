#Bài 1
#Viết chương trình nhập 2 số, chia số thứ nhất cho số thứ hai, xử lý các lỗi có thể xảy ra.
try:
    a = int(input("Nhập số chia: "))
    b = int(input(" Nhập số bị chia: "))
    c = a / b
    print ("Kết quả là : " ,c)
except ZeroDivisionError:
    print("Lỗi: không được chia cho 0")
except ValueError:
    print("Lỗi: Vui lòng nhập số hợp lệ")