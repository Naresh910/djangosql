# Generated by Django 2.2.1 on 2019-05-11 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stud_app', '0013_auto_20190511_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='emp_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='emp_detail',
            name='user_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
