# Generated by Django 3.2.9 on 2022-01-07 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20220107_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='product/', verbose_name='사진'),
        ),
    ]
