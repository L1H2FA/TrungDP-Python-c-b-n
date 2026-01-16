#Bài tập 5: 
#Viết hàm nhận vào 3 số nguyên bất kỳ, trả về số nguyên có giá trị nhỏ nhất.
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
def giaTrinhonhat (a,b,c):
    nhoNhat = a
    if b < nhoNhat:
        nhoNhat = b
    if c < nhoNhat:
        nhoNhat = c
    return nhoNhat
print(" Số nhỏ nhất là: ", giaTrinhonhat(a,b,c))