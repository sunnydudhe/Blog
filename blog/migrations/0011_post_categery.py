# Generated by Django 4.2.4 on 2023-10-16 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.categories'),
        ),
    ]