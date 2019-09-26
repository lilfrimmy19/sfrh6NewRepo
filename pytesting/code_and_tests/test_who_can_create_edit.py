import who_can_create_edit

#testing who can edit and create documents
def test_create_and_edit():

	assert who_can_create_edit.create("professorGoggins") == "You can create", "You don't have permission to create"
	assert who_can_create_edit.edit("taCaleb") == "You can edit", "You don't have permissions to edit"
