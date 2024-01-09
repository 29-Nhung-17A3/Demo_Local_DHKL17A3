x,y = 5,0
try:
    print('x/y', x/y)
except ZeroDivisionError as ex:
    print('Error:', ex)    
finally:
    print('x+y=',x+y)  
    print('x-y=',x-y) 
    print('x*y=',x*y)  
