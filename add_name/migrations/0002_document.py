# Generated by Django 5.1.4 on 2025-01-19 10:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_name', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='documents/')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='add_name.name')),
            ],
        ),
    ]
