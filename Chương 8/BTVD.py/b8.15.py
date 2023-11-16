print("Chương trình tính tổng N số nguyên")
tong = 0
while True: 
    so = int(input("Nhập một số nguyên (kết thức là số 0): "))
    if so == 0:
        break
    tong += so
print("S =",tong)