# Generated by Django 5.1.1 on 2024-09-12 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default=1, upload_to=' images/'),
            preserve_default=False,
        ),
    ]
