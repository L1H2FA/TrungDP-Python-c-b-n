#Bài tập 3: 
#Tạo 1 List có tên là ‘’numbers’’ trong Python và cho người dùng nhập vào 10 phần tử số nguyên sau đó hiển thị tổng tất cả phần tử có giá trị > 10
numbers = []
for i in range(10):
        n = int(input(f"Nhập số nguyên thứ {i+1}: "))
        numbers.append(n)
# Tính tổng các phần tử > 10
tong = 0
for x in numbers:
    if x > 10:
         tong += x
print ("Danh sách numbers:", numbers)
print ("Tổng các phần tử lớn hơn 10 là:", tong)
    