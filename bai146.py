#Bài 6: Chuyển đổi Tuple ↔ List
#Cho tuple:
#t = (10, 20, 30, 40)
#1.	Chuyển tuple thành list.
#2.	Thêm số 50 vào list.
#3.	Chuyển list đó lại thành tuple và in ra kết quả.
t = (10, 20, 30, 40)
#1.	Chuyển tuple thành list.
Li = list(t)
print("Tuple đã chuyển sang list: ",Li)
#2.	Thêm số 50 vào list.
Li.append(50)
#3.	Chuyển list đó lại thành tuple và in ra kết quả.
t_newconvert = tuple(Li)
print("Tuple mới:",t_newconvert)