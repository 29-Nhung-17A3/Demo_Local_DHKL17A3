try:
    value = int(input("Nhập một số"))
    result = 10 / value
except ValueError:
    print("Đó không phải là một giá trị số hợp lệ")
except ZeroDivisionError:
    print("Lỗi chia cho 0")  
except:
    print("Một lỗi không xác định đã xảy ra")  
else:
    print("Không có lỗi xảy ra. Kết quả là:", result)        
finally:
    print("Hoàn thành xử lý ngoại lệ")    
