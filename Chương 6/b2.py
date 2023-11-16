# Nhập thông tin hàng hóa
ten_hang = "Sữa hộp Vina Milk"
so_luong = 5
don_gia = 25000

# Tính tiền phải trả
tien_phai_tra = so_luong * don_gia

# Xuất kết quả
print("Tên hàng:", ten_hang)
print("Số lượng:", so_luong)
print("Đơn giá:", don_gia, "vnđ")
print("Tiền phải trả:", "{:,}".format(tien_phai_tra), "vnđ")