def tinh_S(n, x):
    """
    Tính giá trị của biểu thức S = (x^2 + 1)^n.
    """
    S = (x**2 + 1)**n
    return S

def main():
    # Nhập giá trị của n và x từ người dùng
    n = int(input("Nhập giá trị của n: "))
    x = float(input("Nhập giá trị của x: "))

    # Tính giá trị của S và hiển thị kết quả
    ket_qua = tinh_S(n, x)
    print(f"Giá trị của S = (x^2 + 1)^n là: {ket_qua}")

if __name__ == "__main__":
    main()