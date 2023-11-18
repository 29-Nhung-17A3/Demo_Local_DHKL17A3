# Sử dụng phương thức lambda để tính diện tích và chu vi hình tròn
tinh_dien_tich_hinh_tron = lambda r: 3.14 * r**2
tinh_chu_vi_hinh_tron = lambda r: 2 * 3.14 * r

# Sử dụng phương thức lambda để tính diện tích và chu vi hình chữ nhật
tinh_dien_tich_hinh_chu_nhat = lambda a, b: a * b
tinh_chu_vi_hinh_chu_nhat = lambda a, b: 2 * (a + b)

def main():
    # Nhập thông tin từ người dùng
    r = float(input("Nhập bán kính hình tròn: "))
    a = float(input("Nhập chiều dài hình chữ nhật: "))
    b = float(input("Nhập chiều rộng hình chữ nhật: "))

    # Tính và hiển thị diện tích và chu vi hình tròn
    dien_tich_hinh_tron = tinh_dien_tich_hinh_tron(r)
    chu_vi_hinh_tron = tinh_chu_vi_hinh_tron(r)
    print(f"Diện tích hình tròn là: {dien_tich_hinh_tron:.2f}")
    print(f"Chu vi hình tròn là: {chu_vi_hinh_tron:.2f}")

    # Tính và hiển thị diện tích và chu vi hình chữ nhật
    dien_tich_hinh_chu_nhat = tinh_dien_tich_hinh_chu_nhat(a, b)
    chu_vi_hinh_chu_nhat = tinh_chu_vi_hinh_chu_nhat(a, b)
    print(f"Diện tích hình chữ nhật là: {dien_tich_hinh_chu_nhat:.2f}")
    print(f"Chu vi hình chữ nhật là: {chu_vi_hinh_chu_nhat:.2f}")

if __name__ == "__main__":
    main()