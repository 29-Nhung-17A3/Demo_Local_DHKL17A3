def inches_to_meters(inches):
    return inches * 0.0254
def main():
    my_list = [74, 74, 72, 72, 73, 69, 69, 71, 76, 71]
    while True:
        try:
            height = float(input("Nhập chiều cao (inch) (nhập bất kỳ ký tự để dừng): "))
            my_list.append(height)
        except ValueError:
            break
    print(f"List chiều cao (inch) của bạn: {my_list}")
    heights_in_meters = [inches_to_meters(height) for height in my_list]
    print(f"3 chiều cao đầu tiên: {heights_in_meters[:3]}")
    print(f"3 chiều cao cuối cùng: {heights_in_meters[-3:]}")
    if heights_in_meters:
        avg_height = sum(heights_in_meters) / len(heights_in_meters)
        print(f"Chiều cao trung bình: {avg_height} mét")
    else:
        print("List rỗng, không có chiều cao trung bình")
    if heights_in_meters:
        max_height = max(heights_in_meters)
        min_height = min(heights_in_meters)
        print(f"Chiều cao lớn nhất: {max_height} mét")
        print(f"Chiều cao nhỏ nhất: {min_height} mét")
    else:
        print("List rỗng, không có chiều cao lớn nhất và nhỏ nhất")
    ascending_list = sorted(heights_in_meters)
    descending_list = sorted(heights_in_meters, reverse=True)
    print(f"List chiều cao tăng dần: {ascending_list}")
    print(f"List chiều cao giảm dần: {descending_list}")
if __name__ == "__main__":
    main()
