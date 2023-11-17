# Generated by Django 4.2.4 on 2023-11-07 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=25)),
                ('image', models.ImageField(upload_to='shop/images')),
            ],
        ),
    ]
