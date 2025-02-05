# Generated by Django 5.1 on 2024-10-04 17:35

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
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_provider', models.BooleanField(default=False)),
                ('is_client', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(default='unknown', max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('alternate_phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='user_pics/')),
                ('aadhar_number', models.CharField(blank=True, max_length=12, null=True)),
                ('bank_account', models.CharField(max_length=20, null=True)),
                ('ifsc_code', models.CharField(max_length=11, null=True)),
                ('govt_id', models.FileField(blank=True, null=True, upload_to='govt_ids/')),
                ('experience', models.TextField(blank=True, null=True)),
                ('availability', models.CharField(blank=True, choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('temporary', 'Temporary')], max_length=50, null=True)),
                ('hourly_salary', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('about_me', models.TextField(blank=True, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('service_types', models.ManyToManyField(blank=True, to='users.servicetype')),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(default='unknown', max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('alternate_phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='user_pics/')),
                ('aadhar_number', models.CharField(blank=True, max_length=12, null=True)),
                ('bank_account', models.CharField(max_length=20, null=True)),
                ('ifsc_code', models.CharField(max_length=11, null=True)),
                ('govt_id', models.FileField(blank=True, null=True, upload_to='govt_ids/')),
                ('availability', models.CharField(blank=True, choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('temporary', 'Temporary')], max_length=50, null=True)),
                ('about_work', models.TextField(blank=True, null=True)),
                ('service_needed', models.ManyToManyField(blank=True, to='users.servicetype')),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.userprofile')),
            ],
        ),
    ]
