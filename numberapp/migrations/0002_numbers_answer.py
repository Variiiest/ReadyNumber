# Generated by Django 3.2 on 2022-01-07 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('numberapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='numbers',
            name='answer',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]