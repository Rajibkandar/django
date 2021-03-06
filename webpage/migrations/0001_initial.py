# Generated by Django 4.0.3 on 2022-04-11 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_description', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
                ('product_date', models.DateField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
