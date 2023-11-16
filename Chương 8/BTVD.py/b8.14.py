def tinh_tong(n):
    tong = 0
    for i in range(n):
        so = int(input("Nhập số thứ {}: ".format(i+1)))
        tong += so
    return tong

n = int(input("Nhập số lượng số nguyên: "))
print("Tổng của {} số nguyên là: {}".format(n, tinh_tong(n)))