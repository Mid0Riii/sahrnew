import xadmin
from .models import Signs
from utils.xadmin.plugins import add_html, change_update_to_detail,new_filter,custom_buttons
from xadmin.views import DetailAdminView, ListAdminView,ModelFormAdminView,UpdateAdminView,CreateAdminView

@xadmin.sites.register(Signs)
class SignsAdmin(object):
    show_bookmarks = False

    Add_sign_create_iframe_allow = True
    Add_sign_edit_iframe_allow = True
    Add_sign_detail_iframe_allow = True

    change_update_to_detail_allow=True
    Approval_custom_buttons_allow = True
    list_display=['title','director','createDate','get_status_name']


xadmin.site.register_plugin(add_html.Add_sign_create_iframe,CreateAdminView)
xadmin.site.register_plugin(add_html.Add_sign_edit_iframe,UpdateAdminView)
xadmin.site.register_plugin(add_html.Add_sign_detail_iframe,DetailAdminView)
xadmin.site.register_plugin(change_update_to_detail.Change_update_to_detail, ListAdminView)
xadmin.site.register_plugin(custom_buttons.Approval_custom_buttons,ListAdminView)
