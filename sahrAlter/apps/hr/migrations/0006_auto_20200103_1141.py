# Generated by Django 2.0.13 on 2020-01-03 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0005_auto_20200103_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='personal_birth_date',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='出生日期'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='personal_folk',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='民族'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='personal_id_num',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='身份证号'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='personal_is_marry',
            field=models.CharField(blank=True, choices=[('未婚', '未婚'), ('已婚', '已婚'), ('丧偶', '丧偶'), ('离异', '离异')], max_length=4, null=True, verbose_name='婚姻情况'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='personal_phone',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='电话'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='personal_reg_location',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='户籍'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='personal_soc_ins',
            field=models.CharField(blank=True, choices=[('是', '是'), ('否', '否')], max_length=2, null=True, verbose_name='是否缴纳社保'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='personal_soc_ins_id',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='社保卡号'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='personal_status',
            field=models.CharField(blank=True, choices=[('中共党员', '中共党员'), ('中共预备党员', '中共预备党员'), ('共青团员', '共青团员'), ('民革党员', '民革党员'), ('民盟党员', '民盟党员'), ('民建会员', '民建会员'), ('民进会员', '民进会员'), ('农工党党员', '农工党党员'), ('致公党党员', '致公党党员'), ('九三学社社员', '九三学社社员'), ('台盟盟员', '台盟盟员'), ('无党派人士', '无党派人士')], max_length=10, null=True, verbose_name='政治面貌'),
        ),
    ]
