from collections import OrderedDict

students = ['denzel', 'samuel', 'billie', 'joel', 'armajaa', 'ralph', 'frank', 'john']

def search_student(studentname):
	
	if studentname in students:
		return "Student Found"
	else:
		return "Student Not Found"

