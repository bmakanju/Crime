# Generated by Django 3.2.6 on 2021-09-29 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20210929_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bird',
            field=models.CharField(blank=True, default='Not on Twitter yet', max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fb',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gb',
            field=models.CharField(blank=True, default='Not on Google +', max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gram',
            field=models.CharField(blank=True, default='Not on Instagram yet', max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='linkin',
            field=models.CharField(blank=True, default='Not on LinkedIn Yet', max_length=500),
        ),
    ]
