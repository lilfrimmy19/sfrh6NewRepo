import pytest

def validtelephone(phonenumber):
	if len(phonenumber) != 12:
		return False

	for i in range(12):
		if i in [3,7]:
			if phonenumber[i] != '-':
				return False
		elif not phonenumber[i].isalnum():
			return False
	
	return True

