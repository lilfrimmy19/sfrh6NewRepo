import count_occurences
from count_occurences import count

#testing for the length of a password
def test_count(count):

	assert count >= 12
	assert count <= 24
