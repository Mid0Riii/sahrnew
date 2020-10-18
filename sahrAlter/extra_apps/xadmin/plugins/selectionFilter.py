import xadmin
from xadmin.views import BaseAdminPlugin
from xadmin.views.detail import DetailAdminView
from xadmin.views.edit import CreateAdminView,UpdateAdminView
"""
    此插件用于实现二级联动查询
"""


class DutyFilter(BaseAdminPlugin):
    duty_filter_allow = False

    def init_request(self, *args, **kwargs):
        return bool(self.is_execute)

    def get_context(self, context):
        return context

    def get_media(self, media):
        path = self.request.get_full_path()
        current_uri = '{scheme}://{host}'.format(scheme=self.request.scheme, host=self.request.get_host())

        if "add" in path or "update" in path:
            media = media + self.vendor('selection.control.js')
        return media


# xadmin.site.register_plugin(DutyFilter, CreateAdminView)
# xadmin.site.register_plugin(DutyFilter,UpdateAdminView)
