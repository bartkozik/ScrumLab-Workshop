# Generated by Django 3.2.15 on 2022-08-05 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dayname',
            name='order',
        ),
    ]
