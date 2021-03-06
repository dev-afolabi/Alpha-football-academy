# Generated by Django 2.1.5 on 2019-02-11 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=28)),
                ('lastname', models.CharField(max_length=28)),
                ('programe_option', models.CharField(choices=[('ft', 'Fulltime Football Program'), ('sc', 'Short-Course Football Programe'), ('tr', 'Showcase Matches(Try-outs)')], max_length=28)),
                ('submitted', models.DateField(auto_now_add=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
            ],
        ),
    ]
