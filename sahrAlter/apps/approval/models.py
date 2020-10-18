from django.db import models
from .tools import modelTools
# Create your models here.
class JudgeFiles(models.Model):
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '签单文件表'
        verbose_name_plural = verbose_name
    object = models.Manager()
    file = models.FileField(upload_to='judgefiles',null=True,blank=True,verbose_name='签单文件')
    name = models.CharField(max_length=100,verbose_name="文件名",blank=True,null=True)


class Signs(models.Model):
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '签单'
        verbose_name_plural=verbose_name
    objects = models.Manager()
    title = models.CharField(max_length=100,verbose_name="待审批签单名")
    createDate = models.DateField(verbose_name="行文日期")
    createAca = models.CharField(max_length=100,verbose_name='行文单位',default='软件学院')
    director = models.CharField(max_length=100,verbose_name="签单负责人")
    info = models.TextField(verbose_name='事项内容')
    file = models.ManyToManyField(JudgeFiles,related_name='files',verbose_name="相关附件",blank=True)
    dep_person = models.CharField(max_length=100,verbose_name="部门负责人",blank=True,null=True)
    dep_opinion = models.TextField(verbose_name="部门负责人意见",blank=True,null=True)
    dep_judge = models.CharField(max_length=5, verbose_name='部门负责人审批结果', choices=modelTools.set_choices(['通过', '否决']),blank=True,null=True)
    office_person = models.CharField(max_length=100,verbose_name="两办负责人",blank=True,null=True)
    office_opinion = models.TextField(verbose_name="两办负责人意见",blank=True,null=True)
    office_judge = models.CharField(max_length=5, verbose_name='两办负责人审批结果', choices=modelTools.set_choices(['通过', '否决']),blank=True,null=True)
    relate_person = models.CharField(max_length=100,verbose_name="相关部门负责人",blank=True,null=True)
    relate_opinion = models.TextField(verbose_name="相关部门负责人意见",blank=True,null=True)
    relate_judge = models.CharField(max_length=5, verbose_name='相关部门负责人审批结果', choices=modelTools.set_choices(['通过', '否决']),blank=True,null=True)
    vice_person = models.CharField(max_length=100,verbose_name="分管校领导",blank=True,null=True)
    vice_opinion = models.TextField(verbose_name="分管校领导意见",blank=True,null=True)
    vice_judge = models.CharField(max_length=5, verbose_name='分管校领导审批结果', choices=modelTools.set_choices(['通过', '否决']),blank=True,null=True)
    aca_person = models.CharField(max_length=100,verbose_name="校领导",blank=True,null=True)
    aca_opinion = models.TextField(verbose_name="校领导会签意见",blank=True,null=True)
    aca_judge = models.CharField(max_length=5, verbose_name='校领导会签结果', choices=modelTools.set_choices(['通过', '否决']),blank=True,null=True)
    status_code = models.CharField(max_length=5,verbose_name='状态码',blank=True,null=True)
    # TODO 用状态码表示签单状态
    # 000 签单驳回 100部门审批 101两办审批 102相关部门审批 103分管校领导审批 104校领导审批 200通过
    # TODO xadmin对象级权限控制

    def get_status_name(self):
        status_dict={"000":"签单驳回","100":"部门审批","101":"两办审批","102":"相关部门审批",
                     "103":"分管校领导审批","104":"校领导审批","200":"审批通过"}
        return status_dict[self.status_code]
    get_status_name.short_description = u'签单状态'
    get_status_name.allow_tags = get_status_name.is_column = True

