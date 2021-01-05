# Generated by Django 2.2.12 on 2021-01-05 17:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_auto_20210104_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Employee')),
            ],
            options={
                'verbose_name': '管理员表',
                'verbose_name_plural': '管理员表',
            },
        ),
        migrations.RenameField(
            model_name='audit',
            old_name='publisher',
            new_name='applicant',
        ),
        migrations.AlterField(
            model_name='audit',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Manager'),
        ),
        migrations.AlterField(
            model_name='audit',
            name='num',
            field=models.CharField(max_length=18, primary_key=True, serialize=False, unique=True, verbose_name='申请编号'),
        ),
        migrations.AlterField(
            model_name='child',
            name='enter_time',
            field=models.DateField(default=datetime.datetime(2021, 1, 5, 17, 18, 26, 202734), verbose_name='入院时间'),
        ),
        migrations.AlterField(
            model_name='to_dolist',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Manager'),
        ),
    ]
