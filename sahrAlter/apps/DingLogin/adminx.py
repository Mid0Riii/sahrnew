import xadmin
from xadmin import views
from xadmin.util import static
from xadmin.views import ListAdminView
from django.utils.translation import gettext, gettext_lazy as _
from import_export import resources,fields
from import_export.widgets import ForeignKeyWidget
from xadmin import site
from django.contrib.auth import get_user_model
from xadmin.layout import Fieldset, Main, Side
from django.utils.translation import ugettext as _

UserCustom = get_user_model()

class UserCustomAdmin(object):
    # TODO: 补全
    class UserResources(resources.ModelResource):
        class Meta:
            model = UserCustom
            fields = ('id','username','password',)
    import_export_args = {'import_resource_class': UserResources,
                          }
    # list_display = ['username']
    # search_fields = ['username']
    # list_filter = ['username']
    # model_icon = 'fa fa-user'

# xadmin.site.unregister(UserCustom)
# xadmin.site.register(UserCustom, UserCustomAdmin)
