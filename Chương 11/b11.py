def process_tuple():
    # Tạo tuple với 10 phần tử chuỗi bất kì
    my_tuple = ('red', 'green', 'yellow', 'blue', 'black', 'white', 'pink', 'orange', 'red', 'blue')

    # Nhập index dương hoặc âm
    index = int(input("Nhập index (0 <= index < 10 hoặc -1 >= index >= -10): "))

    # Kiểm tra giá trị hợp lệ của index
    if index >= 0:
        if index >= 10:
            print("Index không hợp lệ. Thoát chương trình.")
            return
        mirror_index = -index - 1
    else:
        if index <= -10:
            print("Index không hợp lệ. Thoát chương trình.")
            return
        mirror_index = abs(index) - 1

    # In giá trị của phần tử trong tuple có index dương và âm đã nhập
    print(f"Phần tử tại index {index}: {my_tuple[index]}")
    print(f"Phần tử tại index âm {mirror_index}: {my_tuple[mirror_index]}")

    # Nhập chuỗi cần tìm
    s_find = input("Nhập chuỗi cần tìm: ")

    # Tìm và đếm số lần xuất hiện của s_find trong tuple
    count_s_find = my_tuple.count(s_find)
    print(f"Số lần xuất hiện của '{s_find}' trong tuple: {count_s_find}")

# Gọi hàm để thực hiện chương trình
process_tuple()
