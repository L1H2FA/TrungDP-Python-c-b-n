#Bài tập 8: Tính lãi suất ngân hàng
#Yêu cầu: Viết chương trình Python cho phép người dùng nhập vào: :
#Nhập số tiền gửi (float)
#Nhập số năm gửi (int)
#Nhập lãi suất năm (%)
#Tính tiền lãi và tổng tiền sau số năm với lãi suất gộp hàng năm thông qua công thức: 
#Tổng tiền = gốc * (1 + lãi suất/100)^năm
soTiengui = float(input("Nhập số tiền gửi:"))
soNamgui = int(input("Nhập số năm gửi:"))
soLaisuat = float(input("Nhập lãi suất:"))
tongTienlai = soTiengui * (1 + soLaisuat/100) ** soNamgui 
print ("Tổng tiền lãi là:",tongTienlai)