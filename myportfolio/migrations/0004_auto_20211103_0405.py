# Generated by Django 3.2.6 on 2021-11-03 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0003_auto_20211102_0405'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default='NAME', max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(max_length=2000),
        ),
    ]
