#Bài tập 1: 
#Tạo 1 List có tên là ‘’numbers’’ trong Python và cho người dùng nhập vào 10 phần tử số nguyên sau đó hiển thị List này ra màn hình
numbers = []
for i in range (10):
    numbers.append(int(input(f"Nhập số nguyên thứ {i+1}:")))
print("\nDanh Sách numbers:")
for x in numbers:
    print(x, end = " ")
    