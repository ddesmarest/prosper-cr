"""
Temporary user creation tool
"""
from mongoengine import connect
from server.db.user import User
from server.db.workspace import Workspace
from server.db.template.field import UserFieldGroup, UserField

connect('prosper-cr')
me = User(email='ddesmarest@gmail.com', first_name='David',
     last_name='Desmarest').set_password('david').save()
for workspace in [u'Peinture', u'Peinture Musee', u'Peinture Particulier']:
    new_workspace = Workspace(name=workspace)
    new_workspace.users = [me]
    new_workspace.field_groups = []
    group = UserFieldGroup(name='Identification')
    group.fields = []
    new_workspace.field_groups.append(group)    
    group.fields.append(UserField(name='Title', container='string', tooltip='Title of the stuff').initialize())
    group.fields.append(UserField(name='Author', container='string', tooltip='Author of the stuff').initialize())
    group.save()
    new_workspace.save()
    print new_workspace.name, "created"