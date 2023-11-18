def sign(x):
    """
    In ra giá trị theo dấu của số x.
    """
    if x > 0:
        return f"{x} là số dương."
    elif x < 0:
        return f"{x} là số âm."
    else:
        return f"{x} là số không."

def main():
    # Nhập giá trị x từ người dùng
    x = float(input("Nhập một số: "))

    # In ra giá trị theo dấu của số x
    ket_qua = sign(x)
    print(ket_qua)

if __name__ == "__main__":
    main()