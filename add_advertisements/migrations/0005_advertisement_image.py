# Generated by Django 4.2.4 on 2023-08-27 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_advertisements', '0004_advertisement_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(default='', upload_to='advetisements/', verbose_name='изобажение'),
            preserve_default=False,
        ),
    ]