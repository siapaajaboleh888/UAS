# Generated by Django 4.2.6 on 2023-11-27 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_description_alter_product_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gambar_produk',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
