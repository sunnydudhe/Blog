# Generated by Django 4.2.4 on 2023-10-26 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_rename_facebook_url_userprofile_facebook_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='profilepicture',
            new_name='picture',
        ),
    ]
