#Bài tập 4: 
#Tạo 1 List có tên là ‘’numbers’’ trong Python và cho người dùng nhập vào 10 phần tử số nguyên sau đó hiển thị có bao nhiêu phần tử > 5

numbers = []
for i in range (10):
        n = int(input(f"Nhập số nguyên thứ {i+1}: "))
        numbers.append(n)
# Hiện thị danh sách phần tử > 5
dem = 0
for x in numbers:
    if x > 5:
        dem += 1
print("\nDanh Sách numbers:",numbers)
# Hiện thị phần tử thử bao nhiêu trong chuổi
print("Số phần tử >5 là: ",dem)

    