#Bài tập 6: 
#Tạo 2 List có tên là ‘’numbers1’’ và ‘’numbers2’’ trong Python 
#Hiển thị kết quả ra màn hình là 2 list này có giống nhau hay không ( giống cả số lượng phần tử và giá trị mỗi phần tử)
numbers1 = []
for i in range (10):
        n = int(input(f"Nhập số nguyên thứ {i}: "))
        numbers1.append(n)
numbers2 = []
for i in range (10):
        n = int(input(f"Nhập số nguyên thứ {i}: "))
        numbers2.append(n)
# Hiện ra kết quả 2 list này giống nhau không
if numbers1 == numbers2:
        print("\n Hai danh sách này giống nhau về số lượng và phần từ:")
else:
        print("\n Hai danh sách này không giống nhau.")
print ("numbers1:", numbers1)
print ("numbers2:", numbers2)