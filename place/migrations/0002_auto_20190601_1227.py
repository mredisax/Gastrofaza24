# Generated by Django 2.1 on 2019-06-01 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=300, verbose_name='Link'),
        ),
    ]