# Generated by Django 2.2 on 2019-04-23 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='changelog',
            old_name='lasttime',
            new_name='addtime',
        ),
        migrations.RenameField(
            model_name='viewparam',
            old_name='lasttime',
            new_name='addtime',
        ),
    ]
