# Generated by Django 2.0.13 on 2020-01-03 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_auto_20200103_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='createTime',
            field=models.DateField(blank=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='department',
            name='creator',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='department',
            name='director',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='负责人'),
        ),
        migrations.AlterField(
            model_name='department',
            name='info',
            field=models.TextField(blank=True, null=True, verbose_name='简介'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='部门名称'),
        ),
    ]
