#Viết chương trình Python cho người dùng nhập vào 3 số nguyên x,y và z. Tính kết quả cho biểu thức x2 + y2 + x3 ra màn hình
x = float(input("Xin nhập giá trị x:"))
y= float(input("Xin nhập giá trị y:"))
z= float(input("Xin nhập giá trị z:"))
ketQua = x**2 + y**2 + z**3
print("Kết quả biểu thức là:",ketQua)