# Generated by Django 5.0.6 on 2024-05-13 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(max_length=50),
        ),
    ]