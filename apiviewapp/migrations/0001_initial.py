# Generated by Django 5.1 on 2024-09-02 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('genre', models.CharField(max_length=50)),
                ('imdb', models.IntegerField()),
                ('director', models.CharField(max_length=50)),
            ],
        ),
    ]
