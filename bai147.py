#Bài 7: Tuple lồng nhau
#Cho tuple:
#students = (
    #("An", 8.5),
    #("Bình", 7.0),
    #("Chi", 9.2))
#1.	In tên và điểm của từng học sinh.
#2.	Tìm học sinh có điểm cao nhất.
students = (
    ("An", 8.5),
    ("Bình", 7.0),
    ("Chi", 9.2)
)
for Ten, Diem in students:
    print("Tên: ",Ten, "Điểm: ",Diem)
#2.	Tìm học sinh có điểm cao nhất.
top_ten, top_Diem = students[0]
for Ten, Diem in students:
    if Diem > top_Diem:      # nếu điểm bạn này lớn hơn điểm cao nhất hiện tại
        top_Diem = Diem      # cập nhật điểm cao nhất
        top_ten = Ten        # cập nhật tên người cao nhất

print("Học sinh điểm cao nhất là:", top_ten, "- Điểm:", top_Diem)