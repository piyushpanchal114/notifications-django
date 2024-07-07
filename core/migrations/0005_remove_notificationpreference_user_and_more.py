# Generated by Django 5.0.6 on 2024-07-06 15:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_notificationpreference_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificationpreference',
            name='user',
        ),
        migrations.RemoveField(
            model_name='notificationtype',
            name='is_email',
        ),
        migrations.RemoveField(
            model_name='notificationtype',
            name='is_mobile',
        ),
        migrations.RemoveField(
            model_name='notificationtype',
            name='is_sms',
        ),
        migrations.AddField(
            model_name='notificationpreference',
            name='notification_type',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='noti_prefs', to='core.notificationtype'),
            preserve_default=False,
        ),
    ]
