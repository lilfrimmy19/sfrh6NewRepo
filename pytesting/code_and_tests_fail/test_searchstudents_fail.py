import searchstudents

#checking if student is in list of students
def test_search_student():
	assert searchstudents.search_student("flo") == "Student Found", "Your search came up empty"
