try:
    x=eval(input("Nhập x/n"))
    y=eval(input("Nhập y/n"))
    Z=x/y
except (NameError, ZeroDivisionError) as er:
    print("Error ", er)
else:
    print('x/y = ', Z)       