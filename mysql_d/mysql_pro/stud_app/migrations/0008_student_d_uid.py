# Generated by Django 2.2.1 on 2019-05-11 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stud_app', '0007_auto_20190511_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_d',
            name='uid',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]