# Generated by Django 4.1.5 on 2023-02-05 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tapp', '0005_rename_name_picture_head_rename_desc_picture_para_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picture',
            old_name='para',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='picture',
            old_name='pic',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='picture',
            old_name='head',
            new_name='name',
        ),
    ]
