# Generated by Django 4.0.4 on 2022-05-27 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0005_alter_image_category_alter_image_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]