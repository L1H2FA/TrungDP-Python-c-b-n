def kyTuso(KTS):
    if len(KTS) !=1: # độ dài không bằng 1
        return False
    return '0' <= KTS <= '9'
KTS = input(" Nhập 1 tự đi: ")
print (kyTuso(KTS))