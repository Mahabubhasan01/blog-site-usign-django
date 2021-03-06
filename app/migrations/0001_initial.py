# Generated by Django 4.0.5 on 2022-07-02 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fetured',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='images')),
                ('info', models.TextField(max_length=500)),
                ('avatar', models.ImageField(upload_to='')),
                ('writter', models.CharField(max_length=100)),
                ('choice', models.CharField(choices=[('Food', 'Food'), ('Beauty', 'Beauty'), ('Travel', 'Travel'), ('Techonology', 'Technology')], max_length=50)),
            ],
        ),
    ]
