# Generated by Django 3.2.3 on 2021-05-26 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210525_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammembers',
            name='biography',
            field=models.TextField(default='', verbose_name='Biography'),
        ),
    ]
