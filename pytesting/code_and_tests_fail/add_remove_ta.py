from collections import OrderedDict

professor = "goggins"

ta_list = ['ta_caleb', 'ta_mark', 'ta_john']

def edit_tas(professor_name, ta_name, option):

	if professor_name == professor:

		if option == "a":
			ta_list.append(ta_name)
			return "TA Added"

		elif option == "r":
	
			if ta_name in ta_list:
				ta_list.remove(ta_name)
				return "TA Removed"
			
			else:
				return "Request Denied"
		
		else:
			return "Request Denied"

	else:
		return "Request Denied"
	
