# Generated by Django 2.1.2 on 2018-12-12 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('mark', models.CharField(max_length=20)),
                ('phone', models.IntegerField(max_length=13)),
            ],
        ),
    ]
