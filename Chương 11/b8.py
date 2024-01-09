def has_lucky_numbers(nums):
    return any(num % 7 == 0 for num in nums)
numbers1 = [2, 14, 9, 21, 5]
numbers2 = [3, 8, 12, 16, 22]
result1 = has_lucky_numbers(numbers1)
result2 = has_lucky_numbers(numbers2)
print(f"Danh sách {numbers1} có chứa số may mắn: {result1}")
print(f"Danh sách {numbers2} có chứa số may mắn: {result2}")
