import xadmin
from .models import CurrentStaff, Department, DismissStaff, AllStaff, Meal_allow, Staff, Visit, Study
from xadmin import views
from .customizeviews.detailLayouts import StaffLayout
from .customizeviews.menuLayouts import set_menu
from utils.xadmin.plugins import add_html, change_update_to_detail, new_filter, custom_buttons, linkage_filter
from xadmin.views import DetailAdminView, ListAdminView, ModelFormAdminView, UpdateAdminView, CreateAdminView
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, BooleanWidget
from django.contrib.auth.models import Group, User


@xadmin.sites.register(views.BaseAdminView)
class BaseSetting(object):
    '''
    主题样式多样化
    '''
    enable_themes = True
    use_bootswatch = True


@xadmin.sites.register(views.CommAdminView)
class GlobalSetting(object):
    # 页头
    site_title = '南昌大学软件学院人事系统'
    # 页脚
    site_footer = 'NCUTEA'

    def get_site_menu(self):
        return set_menu(self)


# 仅做母类，不注册视图
class StaffAdmin(object):
    class VisitInline(object):
        model = Visit
        extra = 1
        classes = ['collapse']

    class StudyInline(object):
        model = Study
        extra = 1
        classes = ['collapse']

    inlines = [VisitInline,StudyInline]
    list_display = ['personal_name', 'personal_gender', 'personal_age', 'personal_id_num', 'work_enter_date',
                    'work_department',
                    'edu_grade', 'work_position', 'work_title', ]
    list_filter = ['work_department', 'personal_status', 'personal_gender', 'personal_age', 'personal_birth_date',
                   'edu_grade',
                   'personal_soc_ins', 'work_title']
    exclude = ['fav_nums']
    read_only_fields = ['personal_age']
    Staff_custom_buttons_allow = True
    # new_filter_allow = True
    show_bookmarks = False
    Linkage_filter_allow = True
    add_html_plugins_allow = True
    list_export = ['xls']


@xadmin.sites.register(Department)
class DepartmentAdmin(object):
    class DepartmentResources(resources.ModelResource):
        class Meta:
            model = Department
            fields = ('id', 'name', 'createTime', 'creator', 'director', 'info')
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            # 模型主键

    import_export_args = {'import_resource_class': DepartmentResources,
                          }
    change_update_to_detail_allow = True
    show_bookmarks = False
    add_html_plugins_allow = True
    list_display = ['name', 'createTime', 'director', 'info']
    list_filter = ['name', 'createTime', 'director']
    model_icon = 'fa fa-users'
    list_export = ['xls']


@xadmin.sites.register(CurrentStaff)
class CurrentStaffAdmin(StaffAdmin):
    model_icon = 'fa fa-check'
    Delete_add_bottom_allow = True
    add_html_plugins_allow = True
    change_update_to_detail_allow = True

    def queryset(self):
        user = self.request.user
        print(user)
        g = Group.objects.get(user=user)
        qs = super().queryset()
        qs = qs.filter(at_post='在职')
        if g.name != "管理员":
            qs = qs.filter(personal_name=user.username)
        return qs

    def get_form_layout(self):
        self.form_layout = StaffLayout
        return super().get_form_layout()


@xadmin.sites.register(DismissStaff)
class DismissStaffAdmin(StaffAdmin):
    Delete_add_bottom_allow = True
    show_bookmarks = False
    model_icon = 'fa fa-times'
    add_html_plugins_allow = True
    Linkage_filter_allow = True
    change_update_to_detail_allow = True

    def queryset(self):
        user = self.request.user
        print(user)
        g = Group.objects.get(user=user)
        qs = super().queryset()
        qs = qs.filter(at_post='离职')
        if g.name != "管理员":
            qs = qs.filter(personal_name=user.username)
        return qs

    def get_form_layout(self):
        self.form_layout = StaffLayout
        return super().get_form_layout()


@xadmin.sites.register(AllStaff)
class AllStaffAdmin(StaffAdmin):
    class StaffResources(resources.ModelResource):
        class DepartmentForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return Department.objects.filter(
                    name__iexact=row["work_department"]
                )

        work_department = fields.Field(
            attribute='work_department',
            column_name='work_department',
            widget=DepartmentForeignWidget(Department, 'name')
        )

        class Meta:
            model = Staff
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = (

                "id",
                "personal_name",
                "personal_gender",
                "personal_id_num",
                "personal_birth_date",
                "personal_is_marry",
                "personal_status",
                "personal_folk",
                "personal_reg_location",
                "personal_soc_ins",
                "personal_soc_ins_id",
                "personal_phone",
                "personal_phone_other",
                "personal_emer_people",
                "personal_emer_phone",
                "personal_current_location",
                "personal_on_market",
                "work_set_rank_date",
                "work_hire_rank_aca_date",
                "work_enter_date",
                "work_dismiss_date",
                "work_department",
                "work_duty",
                "work_duty_hire_date",
                "work_hire_method",
                "work_position",
                "work_title",
                "edu_background",
                "edu_grade",
                "edu_learn_exp",
                "edu_collage_school",
                "edu_undergraduate_school",
                "edu_master_school",
                "edu_doctor_school",
                "edu_postdoctor_school",
                "other_more",
                "other_avatar",
                "at_post"
            )

    import_export_args = {'import_resource_class': StaffResources,
                          }
    show_bookmarks = False
    list_export = ['xls']
    change_update_to_detail_allow = True
    Linkage_filter_allow = True
    model_icon = 'fa fa-user'

    def queryset(self):
        user = self.request.user
        print(user)
        g = Group.objects.get(user=user)
        if g.name == "管理员":
            qs = super().queryset()
        else:
            qs = super().queryset()
            qs = qs.filter(personal_name=user.username)
        return qs

    # duty_filter_allow = True
    def get_form_layout(self):
        self.form_layout = StaffLayout
        return super().get_form_layout()


# @xadmin.sites.register(Meal_allow)
# class MealAdmin(object):
#     show_bookmarks = False
#     Meal_custom_buttons_allow = True
#     list_export = ['xls']
#     list_display = ['id', 'name', 'date', 'consume']
#     list_filter = ['id', 'name', 'date', 'consume']
#     model_icon = 'fa fa-money'


@xadmin.sites.register(Visit)
class VisitAdmin(object):
    pass


# xadmin.site.register_plugin(add_html.Add_html_plugins, DetailAdminView)
xadmin.site.register_plugin(change_update_to_detail.Change_update_to_detail, ListAdminView)
xadmin.site.register_plugin(change_update_to_detail.Delete_add_bottom, ListAdminView)
xadmin.site.register_plugin(new_filter.New_filter, ListAdminView)
xadmin.site.register_plugin(custom_buttons.Staff_custom_buttons, ListAdminView)
xadmin.site.register_plugin(add_html.Add_dep_iframe, DetailAdminView)
xadmin.site.register_plugin(linkage_filter.Linkage_filter, UpdateAdminView)
xadmin.site.register_plugin(linkage_filter.Linkage_filter, CreateAdminView)
xadmin.site.register_plugin(custom_buttons.Meal_custom_buttons, ListAdminView)
