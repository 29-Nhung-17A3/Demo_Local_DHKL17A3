def menu_is_boring(meals):
    for i in range(len(meals) - 1):
        if meals[i] == meals[i + 1]:
            return True
    return False

# Nhập danh sách bữa ăn
meals_1 = ["Redneck Ribs", "Prawn Star", "San Quentin Squid", "Fist Full of Pizza", "Honky Tonk Chicken"]
meals_2 = ["Redneck Ribs", "Prawn Star", "Running Bear Slamon", "Running Bear Slamon", "Honky Tonk Chicken"]

# Xuất danh sách bữa ăn
print("Danh sách bữa ăn 1:", meals_1)
print("Danh sách bữa ăn 2:", meals_2)

# Kiểm tra xem danh sách bữa ăn có boring không
result_1 = menu_is_boring(meals_1)
result_2 = menu_is_boring(meals_2)

# Xuất kết quả
print("Danh sách bữa ăn 1 có boring không?", result_1)
print("Danh sách bữa ăn 2 có boring không?", result_2)
