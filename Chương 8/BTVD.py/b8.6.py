def tinh_tien_di_chuyen(so_km, loai_xe):
    if loai_xe == 4:
        if so_km <= 0.8:
            return 0.8 * 11000
        elif so_km <= 20:
            return 0.8 * 11000 + (20 - so_km) * 12100
        else:
            return 0.8 * 11000 + (20 - 0.8) * 12100 + (so_km - 20) * 10000
    elif loai_xe == 7:
        if so_km <= 0.8:
            return 0.8 * 13000
        elif so_km <= 30:
            return 0.8 * 13000 + (30 - so_km) * 14100
        else:
            return 0.8 * 13000 + (30 - 0.8) * 14100 + (so_km - 30) * 12000

loai_xe = int(input("Cho biết loại xe là 4 chỗ hay 7 chỗ ?"))
so_km = float(input("Nhập số km chạy = "))
time_cho = float(input("Thời gian chờ (phút chờ) = "))

tien_cho = (time_cho - 5) * 0.8 if time_cho >= 5 else 0
tien_di_chuyen = tinh_tien_di_chuyen(so_km, loai_xe)
tien_cuoc = tien_cho + tien_di_chuyen

print(f"Cước phí xe taxi {loai_xe} chỗ của quý khách là {tien_cuoc:.2f}")