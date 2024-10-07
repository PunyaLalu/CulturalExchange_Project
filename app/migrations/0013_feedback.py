# Generated by Django 5.0.3 on 2024-04-02 09:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(default='pending', max_length=20)),
                ('reply', models.CharField(max_length=200, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
    ]
