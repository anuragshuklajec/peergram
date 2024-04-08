# Generated by Django 5.0.4 on 2024-04-08 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customuser')),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.domain')),
            ],
        ),
        migrations.CreateModel(
            name='UserChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customuser')),
            ],
        ),
    ]
