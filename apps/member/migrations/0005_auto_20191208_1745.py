# Generated by Django 2.1.11 on 2019-12-08 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_member_organizations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='organizations',
        ),
        migrations.RemoveField(
            model_name='member',
            name='user',
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]