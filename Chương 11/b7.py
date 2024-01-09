def elementwise_greater_than(L, thresh):
    return [value > thresh for value in L]
L = [1, 2, 3, 4]
thresh = 2
result = elementwise_greater_than(L, thresh)
print(result)

