# Generated by Django 5.0.6 on 2024-07-06 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_notificationpreference_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notificationpreference',
            old_name='notification_type',
            new_name='noti_type',
        ),
    ]
