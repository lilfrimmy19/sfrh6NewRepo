import math
from math import pow

def add(x, y):
	return x+y

def multiply(x, y, z):
	product = x*y*z
	return product

def discriminant(a,b,c):
	
	result = pow(b,2) - (4*a*c)

	return result
