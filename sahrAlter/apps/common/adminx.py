import xadmin
from xadmin import views
from xadmin.util import static
from xadmin.views import ListAdminView

from utils.xadmin.plugins.add_html_to_top import AddHtmlToTopPlugin


@xadmin.sites.register(views.BaseAdminView)
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = False
    user_themes = [
        # {
        #     'name': 'Blank Theme',
        #     'description': '...',
        #     'css': 'themes/material.css',
        #     'thumbnail': '...'
        # }
    ]

    default_theme = static('themes/paper.css')


@xadmin.sites.register(views.CommAdminView)
class GlobalSetting(object):
    site_title = '后台管理系统'
    site_footer = '后台管理系统'

    menu_style = 'default'  # 'accordion'


xadmin.site.register_plugin(AddHtmlToTopPlugin, ListAdminView)
