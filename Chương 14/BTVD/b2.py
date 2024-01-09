def nhap_so_nguyen_duong():
    so_lan_lap_lai = 0
    so_truoc = None
    so_chan_lien_tiep = 0

    while True:
        try:
            so_nhap = int(input("Nhập một số nguyên dương (nhập 0 để kết thúc): "))
            
            if so_nhap < 0:
                raise ValueError("Lỗi số âm!!!")
            elif so_nhap == so_truoc:
                so_lan_lap_lai += 1
                if so_lan_lap_lai == 4:
                    raise ValueError("Lỗi nhập lặp lại!!!")
            else:
                so_lan_lap_lai = 0
            
            if so_nhap % 2 == 0:
                so_chan_lien_tiep += 1
                if so_chan_lien_tiep == 5:
                    raise ValueError("Lỗi nhập chẵn!!!")
            else:
                so_chan_lien_tiep = 0
            
            if so_nhap == 0:
                break
            
            so_truoc = so_nhap
            
        except ValueError as ve:
            if "Lỗi nhập lặp lại!!!" in str(ve) or "Lỗi nhập chẵn!!!" in str(ve):
                print(f"Phát sinh lỗi: {ve}")
            else:
                print("Lỗi nhập số!!!")

try:
    nhap_so_nguyen_duong()
except Exception as e:
    print(f"Lỗi không xác định: {e}")
