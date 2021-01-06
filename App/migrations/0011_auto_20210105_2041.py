# Generated by Django 2.2.12 on 2021-01-05 20:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_auto_20210105_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='height',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2, verbose_name='身高/cm'),
        ),
        migrations.AddField(
            model_name='step_parent',
            name='married',
            field=models.BooleanField(default=False, verbose_name='是否已婚'),
        ),
        migrations.AlterField(
            model_name='child',
            name='edu',
            field=models.CharField(default='文盲', max_length=20, verbose_name='教育水平'),
        ),
        migrations.AlterField(
            model_name='child',
            name='enter_time',
            field=models.DateField(default=datetime.datetime(2021, 1, 5, 20, 41, 24, 86569), verbose_name='入院时间'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='edu',
            field=models.CharField(default='文盲', max_length=20, verbose_name='学历'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='ethnic_groups',
            field=models.CharField(default='汉', max_length=20, verbose_name='民族'),
        ),
    ]
