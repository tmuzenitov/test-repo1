x = int(input('Первое число:'))
y = int(input('Второе число:'))
z = int(input('Третье число:'))

if x == y and y == z and z ==x:
	print(3)

elif x != y and y != z and z != x:
		print(0)
else:
	print(2)