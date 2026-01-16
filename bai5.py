#Bài tập 5: 
#Tạo 1 List có tên là ‘’numbers’’ trong Python và cho người dùng nhập vào 10 phần tử số nguyên. 
#Tiếp tục cho người dùng nhập 1 số n 
#Nếu n tồn tại trong list numbers thì tiến hành xóa giá trị n ra khỏi list number
#sau đó hiển thị có bao nhiêu phần tử > 5

numbers = []
for i in range (10):
        n = int(input(f"Nhập số nguyên thứ {i+1}: "))
        numbers.append(n)
# Nhập thêm một số n
n = int(input("Nhập số n:"))
#Nếu số n có trong danh sách thì xóa đi 
if n in numbers:
        numbers.remove(n)
        print(f"Đã xóa phần tử đã tồn tại{n} khỏi danh sách.")
else:   
        print(f"{n} không có trong danh sách")

# Hiện thị danh sách phần tử > 5
dem = 0
for x in numbers:
    if x > 5:
        dem += 1
print("\nDanh Sách numbers sau khi đã xóa:",numbers)
# Hiện thị phần tử thử bao nhiêu trong chuổi
print("Số phần tử >5 là: ",dem)

    