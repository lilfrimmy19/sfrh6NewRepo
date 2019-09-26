from collections import OrderedDict

editors = ['professorGoggins', 'taCaleb']

def create(name):

	if name in editors:
		if name == "professorGoggins":
			return "You can create"
		else:
			return "You can't create"
	else:
		return "You can't create"

def edit(name):
	
	if name in editors:
		return "You can edit"
	else:
		return "You can't edit"
