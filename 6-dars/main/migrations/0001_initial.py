# Generated by Django 5.0.1 on 2024-01-13 13:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('is_checked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='items/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.region')),
            ],
        ),
    ]
