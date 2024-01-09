def main():
    my_list = [10, 5, -2, 23, 5, 6, 7]
    while True:
        try:
            num = float(input("Nhập số (nhập bất kỳ ký tự để dừng): "))
            my_list.append(num)
        except ValueError:
            break
    print(f"List của bạn: {my_list}")
    total = sum(my_list)
    print(f"Tổng các phần tử trong list: {total}")
    x = float(input("Nhập số x: "))
    if x in my_list:
        count_x = my_list.count(x)
        print(f"{x} xuất hiện trong list {count_x} lần")
    else:
        print(f"{x} không xuất hiện trong list")
    greater_than_x = [num for num in my_list if num > x]
    if greater_than_x:
        print(f"Các số lớn hơn {x} trong list: {greater_than_x}")
    else:
        print(f"Không có số nào lớn hơn {x} trong list")

if __name__ == "__main__":
    main()
