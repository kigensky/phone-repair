# Generated by Django 3.1.7 on 2021-06-10 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0007_auto_20210610_0957'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subject',
            new_name='Operating_System',
        ),
        migrations.RenameField(
            model_name='repair',
            old_name='subject',
            new_name='Operating_System',
        ),
    ]
