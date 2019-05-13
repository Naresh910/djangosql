# Generated by Django 2.2.1 on 2019-05-11 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stud_app', '0006_remove_student_details_register_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_d',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father', models.CharField(max_length=30)),
                ('register_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stud_app.Register_model')),
            ],
        ),
        migrations.DeleteModel(
            name='Student_details',
        ),
    ]