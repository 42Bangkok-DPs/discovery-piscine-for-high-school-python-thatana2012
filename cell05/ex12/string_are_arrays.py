#!/usr/bin/python3
import sys

if len(sys.argv) != 2:
	print("none")
else:
	# string = sys.argv[1]
	length = len(sys.argv[1])
	i = 0
	have_z = False
	for i in range(length):
		if (sys.argv[1][i] == 'z'):
			print("z", sep='', end='')
			have_z = True
		i += 1
	if not have_z:
		print("none")
