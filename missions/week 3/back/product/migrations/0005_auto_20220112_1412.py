# Generated by Django 3.2.9 on 2022-01-12 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20220112_0221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=200, null=True, verbose_name='사이즈')),
                ('color', models.CharField(max_length=100, null=True, verbose_name='색상')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
    ]