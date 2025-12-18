#Bài tập 5: 
#Viết chương trình Python cho phép nhập vào một số nguyên và hiển thị số đó là số chẵn hay số lẻ, nếu người dùng nhập vào số 0 thì kết thúc chương trình
while True:
    n = int(input(" Nhập một số nguyên: "))
    if n == 0:
        print("Chương trình kết thúc")
        break
    elif n % 2 == 0:
        print ("Số chẵn")
    else:
        print("Số lẻ")
    

    