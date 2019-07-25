# Generated by Django 2.1.7 on 2019-07-17 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_notifications_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='actions',
            field=models.TextField(default='[]'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='actor_content_type',
            field=models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'org'), ('model', 'organization')), models.Q(('app_label', 'auth'), ('model', 'user')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notify_content_type',
            field=models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'org'), ('model', 'organization')), models.Q(('app_label', 'auth'), ('model', 'user')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='target_content_type',
            field=models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'org'), ('model', 'organization')), models.Q(('app_label', 'auth'), ('model', 'user')), _connector='OR'), null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.ContentType'),
        ),
    ]