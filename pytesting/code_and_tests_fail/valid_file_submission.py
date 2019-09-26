from collections import OrderedDict

valid_file_types = ['docx', 'pdf', 'doc', 'py']

def validate_file(file):

	file_type = file.split(".", 1)[1]

	if file_type in valid_file_types:
		return "Acceptable File"
	else:
		return "Not Acceptable File"
