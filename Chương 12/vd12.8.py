def some_func():
    print("Bên trong hàm some_func")
    def some_inner_func():
        var = 10
        print("Bên trong hàm some_inner_func(), giá trị của var = ",var)
    #print("Thử in ra var từ bên ngoài hàm some_inner_func()",var)
some_func()