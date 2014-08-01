from ferris import Controller, scaffold


class Songs(Controller):
    class Meta:
        prefixes = ('admin',)
        components = (scaffold.Scaffolding,)

    admin_list = scaffold.list        #lists all posts
    admin_view = scaffold.view        #view a post
    admin_add = scaffold.add          #add a new post
    admin_edit = scaffold.edit        #edit a post
    admin_delete = scaffold.delete    #delete a post