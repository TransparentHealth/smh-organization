# Generated by Django 2.1.11 on 2019-09-18 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_auto_20190717_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='type',
            field=models.TextField(null=True),
        ),
    ]
