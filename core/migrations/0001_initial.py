# Generated by Django 5.0.7 on 2024-07-27 19:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='İçerik')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluştururma Tarihi')),
            ],
            options={
                'verbose_name': 'Hakkımızda',
                'verbose_name_plural': 'Hakkımızda Ayarları',
                'db_table': 'about',
                'ordering': ['-id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OurPurpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='İçerik')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluştururma Tarihi')),
            ],
            options={
                'verbose_name': 'Amacımız',
                'verbose_name_plural': 'Amacımız alanı',
                'db_table': 'our_purpose',
                'ordering': ['-id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True, verbose_name='Başlık')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Tarih')),
            ],
            options={
                'verbose_name': 'Başlık',
                'verbose_name_plural': 'Başlıklar',
                'db_table': 'titles',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=300, null=True, verbose_name='Madde')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.title')),
            ],
            options={
                'verbose_name': 'Yolcular',
                'verbose_name_plural': 'Yolcu uyarıları',
                'db_table': 'userinfo',
                'managed': True,
            },
        ),
    ]