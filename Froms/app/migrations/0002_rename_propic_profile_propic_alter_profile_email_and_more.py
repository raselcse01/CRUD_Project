# Generated by Django 4.2 on 2023-04-12 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='proPic',
            new_name='propic',
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]