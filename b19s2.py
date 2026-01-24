#Bài 2
#Viết hàm đọc file, nếu file không tồn tại thì thông báo lỗi.
def readfile(tenfile):
    try:
        with open(tenfile, "r", encoding="utf-8") as f:
            return  f.read()
    except FileNotFoundError:
        print ("Lỗi: File'{tenfile}' không tồn tại")
        return  None
        