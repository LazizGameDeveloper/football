# Generated by Django 3.2.3 on 2021-05-24 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210524_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='img/blog/', verbose_name='Image 2x1'),
        ),
        migrations.AlterField(
            model_name='coach',
            name='image',
            field=models.ImageField(default='', upload_to='img/coaches/', verbose_name='Photo 1x1'),
        ),
        migrations.AlterField(
            model_name='galleryphoto',
            name='image',
            field=models.ImageField(default='', upload_to='img/clubGallery/', verbose_name='Photo 640x500'),
        ),
        migrations.AlterField(
            model_name='galleryvideo',
            name='video',
            field=models.FileField(default='', upload_to='video/clubGallery', verbose_name='Video'),
        ),
        migrations.AlterField(
            model_name='mainslides',
            name='image',
            field=models.ImageField(default='', upload_to='img/slides/', verbose_name='Slide image'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='image',
            field=models.ImageField(default='', upload_to='img/partners/', verbose_name='Logo'),
        ),
    ]
