#Bài 2: Độ dài Tuple
#Cho tuple:
#t = (3, 7, 1, 9, 4)
#1.	In ra số lượng phần tử của tuple.
#2.	Kiểm tra xem số 7 có nằm trong tuple hay không.
t = (3, 7, 1, 9, 4)
# In ra số lượng phần tử tuple
print(t)
print("Số lượng phần tử : ", len(t))
# Kiểm tra số 7 có nằm trong tuple hay không
if 7 in t:
    print ("Số 7 có nằm trong tuple.")
else:
    print("Số 7 không nằm trong tuple.")