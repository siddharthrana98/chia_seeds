# Generated by Django 4.1.7 on 2023-04-21 15:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offercard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=20)),
                ('from_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('to_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('discount', models.IntegerField(blank=True)),
                ('status', models.CharField(default='True', max_length=20)),
                ('createDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('updateDate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
