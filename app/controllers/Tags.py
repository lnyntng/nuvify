from ferris import Controller, scaffold, messages

class Tags(Controller):
	class Meta:
		prefixes = ('api', 'admin',)
		components = (scaffold.Scaffolding, messages.Messaging,)

	add = scaffold.add
	list = scaffold.list
	view = scaffold.view
	edit = scaffold.edit	
	api_list = scaffold.list
	api_view = scaffold.view
	api_add = scaffold.add
	api_edit = scaffold.edit
	api_delete = scaffold.delete
	admin_list = scaffold.list
	admin_view = scaffold.view
	admin_add = scaffold.add
	admin_edit = scaffold.edit
	admin_delete = scaffold.delete