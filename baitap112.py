#Bài tập 2: 
#Viết hàm tính diện tích, hàm tính chu vi hình tròn. Gọi hàm vừa xây dựng được
import math
r = float(input("Nhập bán kính r:"))
def dientichhinhtron(r):
    return math.pi*r*r
# tinh chu vi hinh tron
def chuvihinhtron(r):
    return 2*math.pi*r
print("S =",dientichhinhtron(r))
print("C =",chuvihinhtron(r))