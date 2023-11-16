print("Các mã loại phòng cho bạn:")
print("1-Standard")
print("2-Superior Garden View")
print("3-Superior Ocean View")
print("4-Garden View Bungalow")
print("5-Pool View Bungalow")
print("6-Family Room")
print("7-Beach Front Bungalow")
print("8-VIP sea View")

a = int(input("Nhập mã loại phòng:"))
b = int(input("Nhập số đêm:"))

if a == 1:
    c = 1260000
elif a == 2:
    c = 1550000
elif a == 3 or a == 4:
    c = 1830000
elif a == 5 or a == 6:
    c = 2120000
elif a == 7:
    c = 2540000
elif a == 8:
    c = 4800000
else:
    print("Vui lòng chọn lại mã loại phòng.")
    c = 0

if c != 0:
    if b == 1:
        print("Giá tiền phải trả là:", c, "đồng.")
    elif b in [2, 3]:
        print("Giá tiền phải trả là:", c * b * 0.75, "đồng.")
    elif b >= 4:
        print("Giá tiền phải trả là:", c * b * 0.7, "đồng.")
    else:
        print("Vui lòng nhập lại số đêm.")