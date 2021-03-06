# Generated by Django 3.2.2 on 2021-08-25 14:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=100)),
                ('s_type', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=13)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('items', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Society',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sector', models.CharField(max_length=100)),
                ('address', models.TextField(blank=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=6)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('phone', models.CharField(max_length=13)),
                ('alternative_phone', models.CharField(blank=True, max_length=13, null=True)),
                ('tower_number', models.CharField(max_length=100)),
                ('flat_no', models.CharField(max_length=100)),
                ('is_varified', models.BooleanField(default=True)),
                ('society', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.society')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('description', models.TextField(blank=True, null=True)),
                ('purchase_year', models.IntegerField(blank=True, null=True)),
                ('model', models.CharField(blank=True, max_length=100, null=True)),
                ('is_activated', models.BooleanField(default=False)),
                ('is_sold', models.BooleanField(default=False)),
                ('is_negotiable', models.BooleanField(default=False)),
                ('posted_at', models.DateTimeField(default=datetime.datetime.now)),
                ('society', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.society')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
