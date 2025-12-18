#Bài tập 4: 
#Viết chương trình Python cho phép nhập vào một số nguyên dương và in ra các số chia hết cho 3 từ 0 đến chính nó. 
n = int(input("Nhập số nguyên dương: "))
print("Các số chia hết cho 3 từ 0 đến", n, "là:")
for i in range (0, n + 1 ):
    if i % 3 == 0:
        print(i)