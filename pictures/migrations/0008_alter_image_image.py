# Generated by Django 4.0.4 on 2022-05-28 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0007_alter_image_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='no image', upload_to='images/'),
        ),
    ]
