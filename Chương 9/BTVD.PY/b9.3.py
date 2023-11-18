def calculate_bmi(weight_kg, height_m):
    """
    Tính chỉ số BMI dựa trên cân nặng (kg) và chiều cao (m).
    """
    if weight_kg <= 0 or height_m <= 0:
        return "Cân nặng và chiều cao phải lớn hơn 0."
    
    bmi = weight_kg / (height_m ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Hiển thị thông điệp dựa trên chỉ số BMI.
    """
    if bmi < 18.5:
        return "Gầy (Underweight)"
    elif 18.5 <= bmi < 25:
        return "Bình thường (Normal weight)"
    elif 25 <= bmi < 30:
        return "Thừa cân (Overweight)"
    else:
        return "Béo phì (Obese)"

def main():
    # Nhập cân nặng và chiều cao từ người dùng
    weight = float(input("Nhập cân nặng (kg): "))
    height = float(input("Nhập chiều cao (m): "))

    # Tính chỉ số BMI
    bmi = calculate_bmi(weight, height)

    # Hiển thị chỉ số BMI và phân loại
    print(f"Chỉ số BMI của bạn là: {bmi:.2f}")
    print("Phân loại cân nặng:", interpret_bmi(bmi))

if __name__ == "__main__":
    main()