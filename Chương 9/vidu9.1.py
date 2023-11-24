def giaithua(n):
    if n==1:
        return 1
    else:
        return (n* giaithua(n-1))
number1 = 5
number2 = int(input("Nhạp số cần tính giai thừa: "))    
print("Giai thừa của", number1, "là", giaithua(number1))
print("Giai thừa của", number2, "là", giaithua(number2))

while True:
num = int(input("Nhập một số: "))
print("Gấp ba của",num,"là",3 * num)
a, b, c, d = map(float, input("24, 12, 3, 11: ").split(','))
max_number = max(a, b, c, d)
min_number = min(a, b, c, d)
print("Số lớn nhất là: {max_number}")
print("số nhỏ nhất là: {min_number}")