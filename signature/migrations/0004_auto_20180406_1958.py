# Generated by Django 2.0.2 on 2018-04-06 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signature', '0003_auto_20180406_1943'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='Aadhaar',
            new_name='aadhaar',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='Phone',
            new_name='phone',
        ),
    ]