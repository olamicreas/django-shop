# Generated by Django 4.0.6 on 2022-09-07 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(default='me.png', upload_to='product_pics'),
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(default='me.png', upload_to='product_pics '),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(default='me.png', upload_to='product_pics '),
        ),
    ]
