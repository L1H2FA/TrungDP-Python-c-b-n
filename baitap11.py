#Bài tập 1: 
#Tạo hàm pow() nhận vào input là một số nguyên. 
#Tính bình phương của số nguyên đó và trả về kết quả
#Hiển thị kết quả ra màn hình. 
def pow(a):
    return a * a
# Nhập một số nguyên
a = int(input("Nhập số nguyên: "))
# Gọi hàm và in kết quả
result = pow(a)
print("Bình phương của",a, "là: ",result)
