# Generated by Django 3.2.3 on 2021-05-26 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_committee'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='committee',
            options={'ordering': ['name', 'last_name'], 'verbose_name': 'Member', 'verbose_name_plural': 'Committee'},
        ),
        migrations.AddField(
            model_name='committee',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Is active'),
        ),
    ]