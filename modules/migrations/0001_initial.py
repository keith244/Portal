# Generated by Django 5.0.6 on 2024-07-17 05:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Applications',
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('file', models.FileField(upload_to='documents')),
            ],
            options={
                'verbose_name_plural': 'Documents',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(max_length=255)),
                ('course', models.CharField(max_length=255)),
                ('institution', models.CharField(max_length=255)),
                ('grad_year', models.DateField(blank=True, null=True)),
                ('addn_courses', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Education',
            },
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('responsibilities', models.TextField()),
                ('requirements', models.TextField()),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': 'Jobs',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('about', models.TextField()),
                ('job', models.CharField(max_length=150)),
                ('twitter', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
                ('linked_in', models.URLField(blank=True)),
                ('github', models.URLField(blank=True)),
                ('phone', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'verbose_name_plural': 'User Profile',
            },
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=254)),
                ('position', models.CharField(max_length=254)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('responsibility', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Work Experience',
            },
        ),
    ]
