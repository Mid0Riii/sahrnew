# Generated by Django 2.0.13 on 2020-08-04 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0012_auto_20200804_0952'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.RemoveField(
            model_name='job',
            name='dep',
        ),
        migrations.AlterField(
            model_name='staff',
            name='personal_birth_date',
            field=models.DateField(blank=True, max_length=128, null=True, verbose_name='出生日期'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='personal_state',
            field=models.CharField(choices=[('在职', '在职'), ('离休', '离休'), ('退休', '退休'), ('内退返岗', '内退返岗'), ('内退', '内退'), ('异地任职', '异地任职'), ('产假', '产假'), ('后勤集团返岗', '后勤集团返岗')], default='在职', max_length=10, verbose_name='职工状态'),
        ),
        migrations.DeleteModel(
            name='Job',
        ),
    ]
