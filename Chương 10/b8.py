from datetime import datetime, timedelta
def process_date(date_str):
    try:
        date_object = datetime.strptime(date_str, '%d-%m-%Y')
        formatted_date = date_object.strftime('%d-%m-%Y')
        print(f"Ngày tháng năm theo định dạng: {formatted_date}")
        leap_year = "phải" if date_object.year % 4 == 0 and (date_object.year % 100 != 0 or date_object.year % 400 == 0) else "không"
        print(f"Năm {date_object.year} {leap_year} là năm nhuận.")
        weekday = date_object.strftime('%A')
        print(f"Ngày {formatted_date} là thứ {weekday}")
        days_in_month = (date_object + timedelta(days=32)).replace(day=1) - date_object.replace(day=1)
        print(f"Tháng {date_object.month} có {days_in_month.days} ngày.")
    except ValueError:
        print("Nhập không hợp lệ. Vui lòng nhập ngày theo định dạng dd-mm-yyyy.")
input_date = input("Nhập ngày (dd-mm-yyyy): ")
process_date(input_date)
 