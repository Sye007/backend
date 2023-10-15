# Generated by Django 4.2.5 on 2023-09-24 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('age', models.IntegerField(default=18)),
                ('active', models.BooleanField(default=True)),
                ('photo', models.ImageField(upload_to='profile.jpg')),
                ('dateregistered', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('aboutme', models.TextField()),
            ],
        ),
    ]
