from ferris import Controller, scaffold, messages

class Albums(Controller):
	class Meta:
		prefixes = ('api',)
		components = (scaffold.Scaffolding, messages.Messaging)

	api_list = scaffold.list
	api_view = scaffold.view
	api_add = scaffold.add
	api_edit = scaffold.edit
	api_delete = scaffold.delete