# Generated by Django 3.1.2 on 2020-12-03 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kuis', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='question_id',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='quiz_id',
            new_name='quiz',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='quiz_id',
            new_name='quiz',
        ),
    ]