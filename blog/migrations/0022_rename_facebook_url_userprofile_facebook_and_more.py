# Generated by Django 4.2.4 on 2023-10-26 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_delete_customuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='facebook_url',
            new_name='facebook',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='instagram_url',
            new_name='instagram',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='twitter_url',
            new_name='twitter',
        ),
    ]
