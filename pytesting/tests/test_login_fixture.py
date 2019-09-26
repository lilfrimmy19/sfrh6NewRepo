import login_fixture
from login_fixture import loginuser
from login_fixture import loginpass

# testing login function
def test_username(loginuser):
	
	assert loginuser == "user123"

# testing password match
def test_password(loginpass):
	
	assert loginpass == "password456"

