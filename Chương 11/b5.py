def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def main():
    my_list = [1, -3, 2, 8, -4, 7]
    while True:
        try:
            value = float(input("Nhập giá trị (nhập bất kỳ ký tự để dừng): "))
            my_list.append(value)
        except ValueError:
            break
    print(f"List của bạn: {my_list}")
    primes = [num for num in my_list if is_prime(num)]
    print(f"Các số nguyên tố trong list: {primes}")
    positive_numbers = [num for num in my_list if num > 0]
    negative_numbers = [num for num in my_list if num < 0]
    if positive_numbers:
        avg_positive = sum(positive_numbers) / len(positive_numbers)
        print(f"Trung bình cộng các số dương trong list: {avg_positive}")
    else:
        print("Không có số dương trong list")
    if negative_numbers:
        avg_negative = sum(negative_numbers) / len(negative_numbers)
        print(f"Trung bình cộng các số âm trong list: {avg_negative}")
    else:
        print("Không có số âm trong list")
    if my_list:
        max_value = max(my_list)
        min_value = min(my_list)
        print(f"Giá trị lớn nhất trong list: {max_value}")
        print(f"Giá trị nhỏ nhất trong list: {min_value}")
    else:
        print("List rỗng, không có giá trị lớn nhất và nhỏ nhất")
    sorted_list = sorted(my_list)
    print(f"List tăng dần: {sorted_list}")

if __name__ == "__main__":
    main()
