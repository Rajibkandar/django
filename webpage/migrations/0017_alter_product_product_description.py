# Generated by Django 4.0.3 on 2022-05-23 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0016_alter_product_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.TextField(max_length=250000),
        ),
    ]