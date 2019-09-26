from collections import OrderedDict

username = "user123321"
password = "password456789"

def loginuser(user_str, pass_str):

	if user_str == username and pass_str == password:
		return "Login Success"
	else:
		 return "Login Failed"

