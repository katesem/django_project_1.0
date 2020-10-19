# Generated by Django 3.1.1 on 2020-10-19 11:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('password', models.CharField(max_length=128)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('role', models.IntegerField(choices=[(0, 'visitor'), (1, 'admin')], default=0)),
            ],
            options={
                'verbose_name_plural': 'Users',
            },
        ),
    ]
