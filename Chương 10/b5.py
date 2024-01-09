def is_valid_zip(zip_code):
    zip_pattern =compile(r'^\d{6}$')
    return bool(zip_pattern.match(zip_code))
user_input = input("Nhập zip mã hóa: ")
if is_valid_zip(user_input):
    print("{user_input} là hợp lệ zip mã hóa.")
else:
    print("{user_input} không phải là hợp lệ zip mã hóa.")







