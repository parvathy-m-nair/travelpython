# Generated by Django 4.1.5 on 2023-01-29 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('img', models.ImageField(upload_to='pictures')),
                ('desc', models.TextField()),
            ],
        ),
    ]
