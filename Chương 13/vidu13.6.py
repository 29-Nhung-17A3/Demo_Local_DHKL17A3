f = open('heights.txt')
data = f.read()
f.close()
lst = data.split(",")
height = [float(item) for item in lst]
height_m = [h*0.0254 for h in height]
mean = sum(height_m)/len(height_m)
print('Chiều cao trung bình :', round(mean,2))
