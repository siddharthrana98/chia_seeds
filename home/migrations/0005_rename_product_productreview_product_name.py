# Generated by Django 4.1.7 on 2023-04-26 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_productreview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productreview',
            old_name='product',
            new_name='product_name',
        ),
    ]
