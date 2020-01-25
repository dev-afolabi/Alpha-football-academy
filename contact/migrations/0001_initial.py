# Generated by Django 2.1.5 on 2019-02-11 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=28)),
                ('subject', models.CharField(max_length=28)),
                ('email', models.EmailField(max_length=255)),
                ('message', models.TextField(max_length=255)),
                ('submitted', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
