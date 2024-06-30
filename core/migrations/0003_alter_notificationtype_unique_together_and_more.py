# Generated by Django 5.0.6 on 2024-06-30 18:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_preference_type_notificationtype_type_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='notificationtype',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='notificationtype',
            name='is_email',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='notificationtype',
            name='is_mobile',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='notificationtype',
            name='is_sms',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='notificationtype',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notificationtype',
            name='type',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.RemoveField(
            model_name='notificationtype',
            name='preference',
        ),
    ]