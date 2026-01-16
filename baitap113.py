#Bài tập 3: 
#Viết hàm tính giai thừa của một số nguyên bất kỳ được đưa vào. Gọi hàm vừa xây dựng được.
#ví dụ về giai thừa: 5! = 1 x 2 x 3 x 4 x 5 = 120
n = int(input("Nhập số nguyên n(> 0): "))
def giaiThua(n):
    if n < 0:
        return None #Không có giai thừa âm
    gt = 1
    for i in range(1, n+1):
        gt *= i
    return gt
ketQua = giaiThua(n)
if ketQua is None:
    print("Không tính được cho giai thừa âm!")
else:
    print(f"{n}! = {ketQua}")

    