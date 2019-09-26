import valid_file_submission

# testing file submission function
def test_validate_file():
	
	assert valid_file_submission.validate_file(".docx") == "Acceptable File", "The file is not supported"
 
	
