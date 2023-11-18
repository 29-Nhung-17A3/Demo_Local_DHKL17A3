def tinh_can(nam):
    can_list = ["Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm"]
    return can_list[nam % 10]

def tinh_chi(nam):
    chi_list = ["Hợi", "Tí", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất"]
    return chi_list[nam % 12]

def tinh_nam_am_lich(nam):
    can = tinh_can(nam)
    chi = tinh_chi(nam)
    return f"{can} {chi}"

def main():
    # Nhập năm dương lịch từ người dùng
    input_year = int(input("Nhập năm dương lịch: "))

    # Tính năm âm lịch và in kết quả
    nam_am_lich = tinh_nam_am_lich(input_year)
    print(f"Năm âm lịch tương ứng với năm {input_year} là {nam_am_lich}.")

if __name__ == "__main__":
    main()