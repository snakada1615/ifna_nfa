# Generated by Django 2.2.5 on 2019-09-19 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feed',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
            ],
        ),
    ]
