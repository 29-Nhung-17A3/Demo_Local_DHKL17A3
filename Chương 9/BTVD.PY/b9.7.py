def chia_nguyen(x, y):
    """
    Trả về phần nguyên của phép chia x cho y.
    """
    if y == 0:
        return "Không thể chia cho 0."
    return x // y

def main():
    # Nhập giá trị x và y từ người dùng
    x = int(input("Nhập giá trị x (số bị chia): "))
    y = int(input("Nhập giá trị y (số chia): "))

    # Tính và hiển thị phần nguyên của phép chia
    ket_qua = chia_nguyen(x, y)
    print(f"Phần nguyên của {x} chia cho {y} là: {ket_qua}")

if __name__ == "__main__":
    main()