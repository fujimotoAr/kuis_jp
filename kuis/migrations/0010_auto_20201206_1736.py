# Generated by Django 3.1.2 on 2020-12-06 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuis', '0009_auto_20201206_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
