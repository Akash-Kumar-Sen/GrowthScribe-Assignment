# Generated by Django 4.0.4 on 2022-04-14 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('details', models.CharField(max_length=500)),
            ],
        ),
    ]
