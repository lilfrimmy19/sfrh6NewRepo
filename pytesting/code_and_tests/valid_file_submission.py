from collections import OrderedDict

valid_file_types = ['.docx', '.pdf', '.doc', '.py']

def validate_file(file_type):
	if file_type in valid_file_types:
		return "Acceptable File"
	else:
		return "Not Acceptable File"
