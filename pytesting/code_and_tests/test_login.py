import login

# testing login function
def test_username():
	
	assert login.loginuser("user123321", "password456789") == "Login Success", "Sorry the credentials you entered were incorrect"

