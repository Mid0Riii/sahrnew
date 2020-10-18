# 用于员工编辑界面的部门\职位二级联动查询
from xadmin.plugins.actions import BaseAdminPlugin
from django.template import loader

class Linkage_filter(BaseAdminPlugin):
    Linkage_filter_allow = True

    def init_request(self, *args, **kwargs):
        # 根据用户是否制定了``OptionClass`` 的同名属性决定是否启动该插件
        return bool(self.Linkage_filter_allow)

    def get_context(self, __):
        # 如果插件方法的第一个参数为 __ ，则 AdminView 方法将作为第一个参数传入，
        # 注意，这时还未执行该方法， 在插件中可以通过 __() 执行，
        # 这样就可以实现插件在 AdminView 方法执行前实现一些自己的逻辑
        return __()

    # 插件拦截了返回 Media 的方法，加入自己需要的 js 文件。

    def get_media(self, media):
        #media.add_js([self.static('/xadmin/js/customize/delete.model.form.js')])
        return media

    # Block Views
    # 在页面中插入 HTML 片段，显示刷新选项。
    # 模型列表模板在templates/xadmin/views/model_list.html
    def block_before_fieldsets(self, context, nodes):
        html = ''
        # context.update({
        #    'options': ['intall', 'unintall']
        # })
        nodes.append(loader.render_to_string('xadmin/customize/linkage_filter.html'))

