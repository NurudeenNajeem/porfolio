# Generated by Django 3.2.8 on 2023-03-15 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0007_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('phone_number', models.TextField()),
                ('email', models.EmailField(max_length=100)),
                ('message', models.CharField(max_length=400)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
