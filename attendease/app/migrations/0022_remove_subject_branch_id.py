# Generated by Django 4.2.11 on 2024-05-14 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_alter_faculty_course_id_alter_faculty_department_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='branch_id',
        ),
    ]
