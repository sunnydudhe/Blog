# Generated by Django 4.2.4 on 2023-10-25 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
