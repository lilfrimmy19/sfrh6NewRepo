import math_functions

# testing add function
def test_add():

	assert math_functions.add(10, 12) == 22
	assert math_functions.add(10, 1) == 11

# testing multiplication function
def test_multiply():

	assert math_functions.multiply(2,5,3) == 30
	assert math_functions.multiply(10,10,2) == 200

# testing discriminant function
def test_discriminant():

	assert math_functions.discriminant(2,2,2) <= 0
	assert math_functions.discriminant(3,9,2) >= 0
 
	
