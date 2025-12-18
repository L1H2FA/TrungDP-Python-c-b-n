#Bài tập 3: 
#Viết chương trình Python cho phép nhập vào một số nguyên dương sau đó hiển thị ra tất cả ước của số đó. 
n = int(input("Nhập một số nguyên dương: "))
print("Các ước của " + str(n) + " là:")
for i in range (2, n+1):
    if n % i == 0:
        print(i)