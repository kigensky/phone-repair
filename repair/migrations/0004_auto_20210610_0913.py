# Generated by Django 3.1.7 on 2021-06-10 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0003_auto_20210609_1622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repair',
            old_name='title',
            new_name='title_problem',
        ),
    ]
