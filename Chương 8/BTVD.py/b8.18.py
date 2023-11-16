def so_hoan_hao(n):
    tong_uoc_so = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc_so += i
    return tong_uoc_so == n

x = int(input("Nhập vào một số: "))
if so_hoan_hao(x):
    print(f"{x} là số hoàn hảo.")
else:
    print(f"{x} không phải là số hoàn hảo.")