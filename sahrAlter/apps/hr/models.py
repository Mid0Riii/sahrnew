from django.db import models
from .tools import modelTools
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from datetime import datetime


class Department(models.Model):
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Department, self).save(*args, **kwargs)
        try:
            p = Group.objects.get(name=self.name)
        except Exception as e:
            p = Group.objects.create(name=self.name)
        finally:
            p.save()

    class Meta:
        verbose_name = '部门'
        verbose_name_plural = verbose_name

    objects = models.Manager()
    name = models.CharField(max_length=50, verbose_name='部门名称', null=True, blank=True)
    createTime = models.DateField(verbose_name='创建时间', null=True, blank=True)
    creator = models.CharField(max_length=20, verbose_name='创建人', null=True, blank=True)
    director = models.CharField(max_length=20, verbose_name='负责人', null=True, blank=True)
    info = models.TextField(verbose_name='简介', null=True, blank=True)


class Staff(models.Model):
    # Staff类为在/离职以及全部员工的母类

    def __str__(self):
        return self.personal_name

    def save(self, *args, **kwargs):
        import datetime
        self.personal_age = int((datetime.date.today() - self.personal_birth_date).days / 365.25)
        super(Staff, self).save(*args, **kwargs)

        UserCustom = get_user_model()
        try:
            p = UserCustom.objects.get_or_create(username=self.personal_name, is_staff=True, is_active=True)
            p.set_password("123456")
            p.is_staff = True
            p.is_active = True
        except Exception as e:
            self.personal_age = 0
        finally:
            p[0].save()

    objects = models.Manager()

    class Meta:
        verbose_name = '员工母类'
        verbose_name_plural = verbose_name

    personal_state = models.CharField(verbose_name='职工状态', max_length=10,
                                      choices=modelTools.set_choices(['在职', '离休', '退休', '内退返岗', '内退',
                                                                      '调离', '辞职', '自动离职', '开除', '去世', '解聘',
                                                                      '疾病不在岗', '疾病在岗', '哺乳假', '拟调离', '内部退养'
                                                                         , '境内研修', '挂校人才中心', '延聘人员', '离岗待退', '境外研修'
                                                                         , '借调挂职', '短期用工', '病事假', '停职创办企业', '其他',
                                                                      '逾期未归', '返聘人员'
                                                                         , '异地任职', '产假', '后勤集团返岗']), default='在职')
    at_post = models.CharField(verbose_name='职工状态', choices=modelTools.set_choices(['在职', '离职']), max_length=10)
    personal_name = models.CharField(verbose_name='姓名', max_length=50)
    personal_gender = models.CharField(verbose_name='性别', choices=modelTools.set_choices(['女', '男']), max_length=1)
    personal_id_num = models.CharField(verbose_name='身份证号', max_length=20, blank=True, null=True)
    personal_birth_date = models.DateField(verbose_name='出生日期', max_length=128)
    personal_age = models.IntegerField(verbose_name="年龄", default=0)
    personal_is_marry = models.CharField(verbose_name='婚姻情况',
                                         choices=modelTools.set_choices(['未婚', '已婚', '丧偶', '离异']), max_length=4,
                                         blank=True, null=True)
    personal_status = models.CharField(verbose_name='政治面貌',
                                       choices=modelTools.set_choices(['中共党员', '中共预备党员', '共青团员',
                                                                       '民革党员', '民盟党员', '民建会员',
                                                                       '民进会员', '农工党党员', '致公党党员',
                                                                       '九三学社社员', '台盟盟员', '无党派人士']), max_length=10,
                                       blank=True, null=True)
    personal_folk = models.CharField(verbose_name='民族', max_length=5, blank=True, null=True)
    personal_reg_location = models.CharField(verbose_name='户籍', max_length=20, blank=True, null=True)
    personal_soc_ins = models.CharField(verbose_name='是否缴纳社保', choices=modelTools.set_choices(['是', '否']), max_length=2,
                                        blank=True, null=True)
    personal_soc_ins_id = models.CharField(verbose_name='社保卡号', max_length=30, blank=True, null=True)
    personal_phone = models.CharField(verbose_name='电话', max_length=12, blank=True, null=True)
    personal_phone_other = models.CharField(verbose_name='其他联系方式', max_length=50, blank=True, null=True)
    personal_emer_people = models.CharField(verbose_name='紧急联系人', max_length=30, blank=True, null=True)
    personal_emer_phone = models.CharField(verbose_name='紧急电话', max_length=20, blank=True, null=True)
    personal_duty_num = models.CharField(verbose_name='考勤号', max_length=128, null=True, blank=True)
    personal_salery_num = models.CharField(verbose_name='工资号', max_length=128, null=True, blank=True)
    personal_current_location = models.CharField(verbose_name='当前住址', max_length=100, blank=True, null=True)
    personal_on_market = models.CharField(verbose_name='人才市场挂编', choices=modelTools.set_choices(['是', '否']),
                                          max_length=3,
                                          blank=True, null=True)
    work_set_rank_date = models.CharField(verbose_name='职称评定时间', max_length=128, blank=True, null=True)
    work_hire_rank_aca_date = models.CharField(verbose_name='院编员工职称聘用时间', max_length=128, blank=True, null=True)
    work_enter_date = models.CharField(verbose_name='入职时间', max_length=128, blank=True, null=True)
    work_dismiss_date = models.CharField(verbose_name='离职时间', max_length=128, blank=True, null=True)
    work_department = models.ForeignKey(Department, verbose_name='部门', on_delete=models.SET_NULL, null=True, blank=True)
    # duty = models.CharField(verbose_name='行政职务', max_length=10, blank=True, null=True)
    work_duty = models.CharField(verbose_name='行政职务', max_length=128, null=True, blank=True)
    work_duty_hire_date = models.CharField(verbose_name='职务聘用时间', max_length=128, blank=True, null=True)
    work_hire_method = models.CharField(verbose_name='聘用方式',
                                        choices=modelTools.set_choices(['校编', '校合同制', '院编', '院聘', '聘书', '其他'])
                                        , max_length=10, blank=True, null=True)
    work_position = models.CharField(verbose_name='岗位', max_length=20,
                                     choices=modelTools.set_choices(['工勤岗', '管理岗', '教学科研岗位']), blank=True, null=True)
    work_title = models.CharField(verbose_name='职称', max_length=10, blank=True, null=True)
    work_title_type = models.CharField(verbose_name='职称类别', max_length=20, blank=True, null=True,
                                       choices=modelTools.set_choices(['正高', '副高', '中级', '助理', '员级', '初期博'
                                                                          , '初期硕', '见习本', '普通工', '技术工一级', '技术工二级',
                                                                       '技术工三级'
                                                                          , '技术工四级', '技术工五级', '学徒期']))
    edu_background = models.CharField(verbose_name='学历', max_length=50, blank=True, null=True)
    edu_grade = models.CharField(verbose_name='学位', choices=modelTools.set_choices(['学士', '硕士', '博士', '专科', '其他']),
                                 max_length=5, blank=True, null=True
                                 )
    edu_has_abroad = models.CharField(verbose_name='有无访学经历', choices=modelTools.set_choices(['有', '无']), max_length=8)
    edu_learn_exp = models.TextField(verbose_name='学习经历', blank=True, null=True)
    edu_collage_school = models.CharField(verbose_name='专科毕业院校及时间', max_length=128, null=True, blank=True)
    edu_undergraduate_school = models.CharField(verbose_name='学士毕业院校及时间', max_length=128, null=True, blank=True)
    edu_master_school = models.CharField(verbose_name='硕士毕业院校及时间', max_length=128, null=True, blank=True)
    edu_doctor_school = models.CharField(verbose_name='博士毕业院校及时间', max_length=128, null=True, blank=True)
    edu_postdoctor_school = models.CharField(verbose_name='博士后毕业院校及时间', max_length=128, null=True, blank=True)
    other_more = models.TextField(verbose_name='备注', blank=True, null=True)
    other_avatar = models.ImageField(verbose_name='员工照片', upload_to='avatar', default='avatar/default.jpg', blank=True,
                                     null=True)


class DismissStaff(Staff):
    class Meta:
        verbose_name = '离职员工'
        verbose_name_plural = '离职员工'
        proxy = True


class AllStaff(Staff):
    class Meta:
        verbose_name = '员工'
        verbose_name_plural = '员工'
        proxy = True


class CurrentStaff(Staff):
    class Meta:
        verbose_name = '在职员工'
        verbose_name_plural = '在职员工'
        proxy = True


class Meal_allow(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '餐补'
        verbose_name_plural = verbose_name

    objects = models.Manager()
    card_id = models.CharField(max_length=20, verbose_name='消费卡号')
    name = models.CharField(max_length=30, verbose_name='姓名')
    date = models.DateField(verbose_name='日期')
    location = models.CharField(max_length=30, verbose_name='消费地点')
    consume = models.CharField(max_length=50, verbose_name='消费金额')


class Visit(models.Model):
    visit_relate_staff = models.ForeignKey(Staff,on_delete=models.CASCADE,null=True,blank=True,verbose_name="关联职工")
    visit_start_time = models.DateField(verbose_name="访学开始时间", null=True, blank=True)
    visit_end_time = models.DateField(verbose_name="访学结束时间", null=True, blank=True)
    visit_country = models.CharField(verbose_name="访学国家", null=True, blank=True,max_length=128)
    visit_school = models.CharField(verbose_name="访学学校",null=True,blank=True,max_length=128)
    visit_major = models.CharField(verbose_name="访学专业",null=True,blank=True,max_length=128)
    visit_info = models.CharField(verbose_name="备注",max_length=128,null=True,blank=True)
    def __str__(self):
        return self.visit_relate_staff

    class Meta:
        verbose_name = "访学信息"
        verbose_name_plural = verbose_name

class Study(models.Model):
    study_relate_staff = models.ForeignKey(Staff,on_delete=models.CASCADE,null=True,blank=True,verbose_name="关联职工")
    study_school = models.CharField(verbose_name="学校",null=True,blank=True,max_length=128)
    study_grade = models.CharField(verbose_name="学位",null=True,blank=True,max_length=128)
    study_major = models.CharField(verbose_name="专业",null=True,blank=True,max_length=128)

    def __str__(self):
        return self.study_relate_staff

    class Meta:
        verbose_name = "学习经历"
        verbose_name_plural = verbose_name