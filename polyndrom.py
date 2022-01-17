# -*- coding: utf-8 -*-
import math

input_value = 0
while input_value <= 1:
	print(u'Введите положительное число')
	try:
		input_value = int(input())
	except:
		"Не корректное число, попробуйте еще"

if input_value%10 == 0 or (input_value < 100 and input_value%11 != 0):
	print("%d не полиндром" % input_value)
	exit()
else:
	arr = [10**x for x in range(1, int(math.log10(input_value)) + 1)]
arr.reverse()
from_end_iter = 1

for i in arr:
	if i > input_value:
		continue
	from_end_iter *= 10
	from_begin = input_value/i
	from_end = input_value%from_end_iter
	if from_end < 10 and from_begin < 10:
		if from_begin == from_end:
			if i == from_end_iter:
				print("%d полиндром" % input_value)
				exit()
			continue
	if from_begin%10 != int(from_end/(from_end_iter/10)):
		print("%d не полиндром" % input_value)
		exit()
	if i == from_end_iter:
		print("%d полиндром" % input_value)
		exit()
		
print("%d полиндром" % input_value)
			
			
