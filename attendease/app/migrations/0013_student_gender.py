# Generated by Django 4.2.11 on 2024-05-07 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_department_department_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
