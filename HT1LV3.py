x1 = float(input('Число 1:'))
x2 = float(input('Число 2:'))
max1 = (x1 > x2) * x1 + (x2 >= x1) * x2
print('Max:', max1)