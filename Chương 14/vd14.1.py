while True:
    try:
        x = int(input("Nhập số X ="))
        break
    except ValueError:
        print('Bị lỗi, xin mời nhập lại')
print("X= ",x)        