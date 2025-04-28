# -*- coding: utf-8 -*-

def	cikar():
	global x
	global y
	x = 5
	y = 6
	return (x-y)

def	carpma():
	return(x*y)

def ustel(a,b):
	if b == 0:
		return 1
	else:
		return a*ustel(a,b-1)
print("ft name kontrolu : ",__name__ == '__main__')
