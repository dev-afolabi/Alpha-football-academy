# Generated by Django 2.1.5 on 2019-02-12 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(error_messages={'unique': 'This E-mail has already been registered'}, max_length=255, unique=True),
        ),
    ]