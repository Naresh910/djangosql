# Generated by Django 2.2.1 on 2019-05-11 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stud_app', '0015_auto_20190511_1206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_d',
            name='register_model',
        ),
        migrations.DeleteModel(
            name='Emp_d',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Student_d',
        ),
    ]
