#Bài tập 2: 
#Tạo 1 List có tên là ‘’numbers’’ trong Python và cho người dùng nhập vào 10 phần tử số nguyên sau đó hiển thị giá trị lớn nhất trong list numbers và vị trí của phần tử đó trong mảng
numbers = []
for i in range(10):
    numbers.append(int(input(f"Nhập số nguyên thứ {i+1}: ")))
# Tìm giá trị lớn nhất
max_value = max(numbers)
# Tìm vị trí của các giá trị lớn nhất
max_positions = []
for i in range(len(numbers)):
    if numbers[i] == max_value:
     max_positions.append(i)
print("list numbers:", numbers)
print("Giá trị lớn nhất:", max_value)
print(" Vị trí của phần tử lớn nhất (index):",max_positions)