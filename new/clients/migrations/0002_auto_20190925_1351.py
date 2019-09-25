# Generated by Django 2.2.5 on 2019-09-25 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='addresss',
            new_name='address',
        ),
        migrations.AlterField(
            model_name='client',
            name='contact',
            field=models.CharField(max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]