# Generated by Django 5.0 on 2024-01-22 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blood_app', '0002_naya'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='naya',
            name='post',
        ),
    ]