# Generated by Django 4.1.7 on 2023-03-29 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0005_emp_tbl_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp_tbl',
            name='password',
            field=models.TextField(default='password'),
        ),
    ]
