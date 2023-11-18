def kiem_tra_so_nguyen_to(x):
    """
    Kiểm tra xem x có phải là số nguyên tố hay không.
    """
    if x < 2:
        return False  # Số nhỏ hơn 2 không phải là số nguyên tố
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False  # Nếu x chia hết cho số nào đó trong khoảng từ 2 đến căn bậc hai của x, thì x không là số nguyên tố
    return True  # Nếu x không chia hết cho số nào trong khoảng từ 2 đến căn bậc hai của x, thì x là số nguyên tố

def main():
    # Nhập giá trị x từ người dùng
    x = int(input("Nhập một số nguyên dương x: "))

    # Kiểm tra xem x có phải là số nguyên tố hay không và hiển thị kết quả
    if kiem_tra_so_nguyen_to(x):
        print(f"{x} là số nguyên tố.")
    else:
        print(f"{x} không là số nguyên tố.")

if __name__ == "__main__":
    main()