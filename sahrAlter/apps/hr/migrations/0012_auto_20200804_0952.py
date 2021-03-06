# Generated by Django 2.0.13 on 2020-08-04 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0011_auto_20200804_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='edu_has_abroad',
            field=models.CharField(choices=[('有', '有'), ('无', '无')], default=1, max_length=8, verbose_name='有无访学经历'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='staff',
            name='edu_undergraduate_school',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='学士毕业院校及时间'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='work_hire_method',
            field=models.CharField(blank=True, choices=[('校编', '校编'), ('校合同制', '校合同制'), ('院编', '院编'), ('院聘', '院聘'), ('聘书', '聘书'), ('其他', '其他')], max_length=10, null=True, verbose_name='聘用方式'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='work_position',
            field=models.CharField(blank=True, choices=[('工勤岗', '工勤岗'), ('管理岗', '管理岗'), ('教学科研岗位', '教学科研岗位')], max_length=20, null=True, verbose_name='岗位'),
        ),
    ]
