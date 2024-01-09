import cmath
def giai_phuong_trinh_bac_2(a, b, c):
    delta = cmath.sqrt(b**2 - 4*a*c)
    x1 = (-b + delta) / (2 * a)
    x2 = (-b - delta) / (2 * a)
    return x1, x2
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
a_str = input("Nhập hệ số a: ")
b_str = input("Nhập hệ số b: ")
c_str = input("Nhập hệ số c: ")
if is_number(a_str) and is_number(b_str) and is_number(c_str):
    a = float(a_str)
    b = float(b_str)
    c = float(c_str)
    nghiem1, nghiem2 = giai_phuong_trinh_bac_2(a, b, c)
    print(f"Nghiệm thứ nhất x1 = {nghiem1}")
    print(f"Nghiệm thứ hai x2 = {nghiem2}")
else:
    print("Vui lòng nhập số hợp lệ.")