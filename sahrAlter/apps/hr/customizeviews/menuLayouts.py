from ..models import CurrentStaff, Department,DismissStaff, AllStaff, Meal_allow,Visit


def set_menu(self):
    return (
        {
            'title': '员工信息管理',
            'perm': self.get_model_perm(CurrentStaff, 'view'),
            'menus':
                (
                    {
                        'title': '在职员工',
                        'url': self.get_model_url(CurrentStaff, 'changelist'),
                        'icon': 'fa fa-check'
                    },
                    {
                        'title': '离职员工',
                        'url': self.get_model_url(DismissStaff, 'changelist'),
                        'icon': 'fa fa-times'
                    },
                    {
                        'title': '全部员工',
                        'url': self.get_model_url(AllStaff, 'changelist'),
                        'icon': 'fa fa-user'
                    },
                    {
                        'title': '访学经历管理',
                        'url': self.get_model_url(Visit, 'changelist'),
                        'icon': 'fa fa-plane'
                    },
                )
        },
        {
            'title': '部门与职位',
            'perm': self.get_model_perm(Department, 'change'),
            'menus':
                (
                    {
                        'title': '部门管理',
                        'url': self.get_model_url(Department, 'changelist'),
                        'icon': 'fa fa-users'
                    },
                )

        },
        {
            'title':'小工具',
            'menus':
                (
                    {
                        'title': '值班考勤统计',
                        'url': '/ncusc/countDuty',
                        'icon': 'fa fa-file-excel-o'
                    },
                )
        }
        # {
        #     'title': '餐补',
        #     'perm': self.get_model_perm(Meal_allow, 'change'),
        #     'menus':
        #         (
        #             {
        #                 'title': '餐补',
        #                 'url': self.get_model_url(Meal_allow, 'changelist'),
        #                 'icon': 'fa fa-money'
        #             },
        #         )
        # },
    )