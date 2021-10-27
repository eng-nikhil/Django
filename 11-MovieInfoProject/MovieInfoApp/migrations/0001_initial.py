# Generated by Django 3.2.7 on 2021-10-16 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rdate', models.DateField(auto_now=True)),
                ('actor', models.CharField(max_length=50)),
                ('actoress', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]