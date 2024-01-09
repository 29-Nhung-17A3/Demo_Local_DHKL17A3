from numbers import Number
def find_min_max(numbers):
    numbers = [x for x in numbers if isinstance(x, Number)]
    if not numbers:
        return None, None
    min_value = min(numbers)
    max_value = max(numbers)

    return min_value, max_value
number_list = [3, 1.5, "abc", 7, 2.8, -5, 10, "xyz"]
min_val, max_val = find_min_max(number_list)
print("Danh sách các số: {number_list}")
print("Giá trị nhỏ nhất: {min_val}")
print("Giá trị lớn nhất: {max_val}")