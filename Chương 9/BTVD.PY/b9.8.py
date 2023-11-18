def kiem_tra_so_hoan_hao(num):
    """
    Kiểm tra xem một số có phải là số hoàn hảo hay không.
    """
    if num <= 0:
        return False  # Số không phải là số hoàn hảo nếu nó nhỏ hơn hoặc bằng 0

    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i

    return sum_of_divisors == num

def main():
    # Nhập giá trị từ người dùng
    num = int(input("Nhập một số nguyên dương: "))

    # Kiểm tra xem số đó có phải là số hoàn hảo hay không và hiển thị kết quả
    if kiem_tra_so_hoan_hao(num):
        print(f"{num} là số hoàn hảo.")
    else:
        print(f"{num} không là số hoàn hảo.")

if __name__ == "__main__":
    main()