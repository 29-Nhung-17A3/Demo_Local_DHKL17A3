def calculate_expression(x, n):
    result = pow((pow(x, 2) + 1), n)
    return result
x_value = 2
n_value = 3
result_value = calculate_expression(x_value, n_value)
print("Giá trị của biểu thức (x^2 + 1)^n với x = {x_value} và n = {n_value} là: {result_value}")
