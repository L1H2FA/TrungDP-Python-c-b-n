#Bài tập 7: 
#Viết hàm nhận vào 1 số nguyên và hiển thị tổng tất cả các số chẵn từ 0 đến chính nó
#ví dụ: người dùng nhập vào số 10 => hiển thị: tổng các số chẵn từ 0 đến 10 là: 30 ( 2 + 4 + 6 + 8+10)
def tongSochanden_n(n):
    tong = 0
    for i in range(0,n+1):
        if i % 2 == 0:  #i chia hết cho 2  -=>số chẵn
             tong += i
    print(f"Tổng các số chắn từ 0 đến {n} là: {tong}")
# Gọi hàm
n = int(input("Nhập số nguyên n: "))
tongSochanden_n(n)