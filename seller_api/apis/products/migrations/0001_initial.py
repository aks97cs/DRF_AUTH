# Generated by Django 3.0.8 on 2020-07-22 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SellerProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sku_code', models.CharField(max_length=200)),
                ('image', models.FileField(upload_to='')),
                ('description', models.TextField()),
            ],
        ),
    ]
