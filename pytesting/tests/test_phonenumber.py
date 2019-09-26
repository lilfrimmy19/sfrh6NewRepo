import phonenumber

#checking the validity of a phonenumber
def test_validtelephone():
	assert phonenumber.validtelephone("563-859-3832") == True
