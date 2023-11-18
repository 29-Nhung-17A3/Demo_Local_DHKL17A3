def tinh_A(n, x):
    """
    Tính giá trị của biểu thức A = (x^2 + x + 1)^n + (x^2 - x + 1)^n.
    """
    A = (x**2 + x + 1)**n + (x**2 - x + 1)**n
    return A

def main():
    # Nhập giá trị của n và x từ người dùng
    n = int(input("Nhập giá trị của n: "))
    x = float(input("Nhập giá trị của x: "))

    # Tính giá trị của A và hiển thị kết quả
    ket_qua = tinh_A(n, x)
    print(f"Giá trị của A = (x^2 + x + 1)^n + (x^2 - x + 1)^n là: {ket_qua}")

if __name__ == "__main__":
    main()