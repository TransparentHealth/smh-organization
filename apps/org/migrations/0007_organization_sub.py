# Generated by Django 2.1.7 on 2019-06-16 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0006_auto_20190616_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='sub',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]