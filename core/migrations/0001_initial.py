# Generated by Django 5.0.6 on 2024-06-30 16:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_email', models.BooleanField(default=True)),
                ('is_mobile', models.BooleanField(default=True)),
                ('is_sms', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NotificationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preference_type', models.CharField(max_length=255)),
                ('frequency', models.CharField(choices=[('p', 'Periodically'), ('i', 'Instantly'), ('r', 'rarely')], default='p', max_length=5)),
                ('preference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.notificationpreference')),
            ],
        ),
    ]
