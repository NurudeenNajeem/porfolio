# Generated by Django 3.2.8 on 2023-03-13 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hire',
            name='phone_number',
            field=models.CharField(max_length=255),
        ),
    ]