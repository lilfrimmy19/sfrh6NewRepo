import pytest

@pytest.fixture
def loginuser():

	username = "user123"

	return username

@pytest.fixture
def loginpass():
	
	password = "password456"

	return password

