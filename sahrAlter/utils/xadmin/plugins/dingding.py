from xadmin.plugins.actions import BaseAdminPlugin
from xadmin.views.website import LoginView
from django.template import loader
from xadmin.sites import site

class dingding_QR_plugins(BaseAdminPlugin):
    dingding_QR_plugins_allow = True

    def init_request(self, *args, **kwargs):
        # 根据用户是否制定了``OptionClass`` 的同名属性决定是否启动该插件
        return True

    # 插件拦截了返回 Media 的方法，加入自己需要的 js 文件。

    def get_media(self, media):
        #media.add_js([self.static('/xadmin/js/customize/delete.model.form.js')])
        return media

    # Block Views
    # 在页面中插入 HTML 片段，显示刷新选项。
    # 模型列表模板在templates/xadmin/views/model_list.html
    def block_form_bottom(self, context, nodes):
        nodes.append(loader.render_to_string('customize/dingdingQR.html'))
        nodes.append("<h1>插入成功</h1>")
        # 将 HTML 片段加入 nodes 参数中


site.register_plugin(dingding_QR_plugins,LoginView)