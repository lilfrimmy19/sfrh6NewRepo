import random

generated = random.randint(1,101)

def checkforprime():

	if generated > 1:

		for n in range(2, generated):
			if(generated % n) == 0:
				return "Not Prime"
				break
		else:
			return "Found Prime"
	else:
		return "Not Prime"
	
