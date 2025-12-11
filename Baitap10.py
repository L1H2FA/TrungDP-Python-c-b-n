#Viết chương trình nhập một giá trị là độ 0C (Celsius) và chuyển nó sang độ 0F (Fahrenheit).
#Công thức quy đổi: °F  =  ( °C × 1.8 ) +  32
nhietDo_C = float(input("nhập nhiệt độ độ C:"))
heSochuyendoiC_F = 1.8
giaTridieuchinh = 32
ketQua = (nhietDo_C * heSochuyendoiC_F) + giaTridieuchinh
print("nhiệt độ F là:",ketQua)
