# Generated by Django 4.2.11 on 2024-05-14 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_subject_branch_id_subject_faculty_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='branch_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.branch'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='faculty_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.faculty'),
        ),
    ]
