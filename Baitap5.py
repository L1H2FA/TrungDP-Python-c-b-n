#Một bưu điện tính tiền sử dụng điện thoại cho khách hàng theo công thức tính tiền thanh toán = đơn giá * số phút + thuê bao. Viết chương trình Python  cho người dùng nhập vào số phút đã gọi và in ra màn hình số tiền khách phải trả? (thuê bao = 20.000, đơn giá = 1.000) 
soPhut = float(input("Nhập số phút:"))
thueBao = 20.000
donGia = 1.000
tongTienthanhtoan = (donGia * soPhut) * thueBao
print("số tiền thanh toán là:",tongTienthanhtoan)