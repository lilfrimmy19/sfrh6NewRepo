import add_remove_ta


# testing for removal of ta by professor
def test_edit_tas():
	
	assert add_remove_ta.edit_tas("gggins", "ta_caleb", "r") == "TA Removed", "Incorrect information provided"
	assert add_remove_ta.edit_tas("goggins", "ta_samuel", "o") == "TA Added", "Incorrect information provided"
