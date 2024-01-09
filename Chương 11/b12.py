# Tạo tuple a và b
a = (3, 1, 2, 4)
b = (5, 7, 6, 8)

# Tạo tuple c là sự kết hợp của các phần tử trong a và b
c = a + b
print(c)

# Tạo tuple d từ tuple c với các phần tử được sắp xếp
d = tuple(sorted(c))
print(d)

# In phần tử thứ 3 của d
print(f"Phần tử thứ 3 của d: {d[2]}")

# In 3 phần tử cuối cùng của d
print(f"3 phần tử cuối cùng của d: {d[-3:]}")
