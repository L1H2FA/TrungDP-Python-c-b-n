#Bài tập 6: 
#Viết hàm nhận vào 1 số nguyên và hiển thị tất cả các số nguyên tố từ 1 đến chính nó
#ví dụ: người dùng nhập vào số 10 => hiển thị: các số nguyên tố từ 1 đến 10 là: 2,3,5,7
def laSonguyento(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def hienThicacsonguyentodenn(n):
    print(f"các số nguyên tố từ 1 đén {n} là: ", end =" ")
    soDau = True
    for k in range (2, n+1):
        if laSonguyento(k):
            if not soDau:
                print(",", end="")
            print(k,end="")
            soDau = False
    print()
n = int(input("Nhập số nguyên n: "))
hienThicacsonguyentodenn(n)
