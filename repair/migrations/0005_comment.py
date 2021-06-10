# Generated by Django 3.1.7 on 2021-06-10 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0004_auto_20210610_0913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('repair', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='repair.repair')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
