l = 109
v = int(input('Введите скорость:'))
t = int(input('Введите время: '))
s = v*t
sВаси = int((s <= l) * s + (s > l) * (s - l))
print('Байкер Вася остановится на отменке:', sВаси)