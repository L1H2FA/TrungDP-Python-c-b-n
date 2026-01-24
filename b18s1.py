#Bài tập 1: 
#Viết chương trình cho người dùng nhập vào 5 phần tử của list, mỗi phần tử là thông tin cá nhân của 1 người, ví dụ:
# [
#[“Nguyễn Văn A”,20, “Đà Nẵng”], 
#[“Nguyễn Văn B”,22, “Nghệ An”], 
#[“Nguyễn Văn C”,40, “Quãng Nam”], 
#[“Nguyễn Văn D”,16, “Huế”], 
#[“Nguyễn Văn E”, 28, “Hà Nội”]
#]
#Viết hàm đọc và ghi dữ liệu đã nhập vào file data.csv
import csv
students = []
for i in range(5):
    print(f"Nhập tên người dùng thứ {i+1}:")
    Ten = input ("Họ và Tên: ")
    Tuoi = input("Tuổi: ")
    Diachi = input("Địa chỉ: ")
    students.append([Ten, Tuoi, Diachi])
# Hàm ghi dữ liệu vào file
def write_to_csv (filename, data):
    with open (filename, mode = 'w', newline = '', encoding ='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Tên", "Tuổi", "Địa chỉ"])
        for student in data:
            writer.writerow(student)
#Hàm đọc dữ liệu
def read_from_csv(filename):
    with open(filename, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
write_to_csv("data.csv", students)
print("\nDữ liệu trong file:")
read_from_csv("data.csv")