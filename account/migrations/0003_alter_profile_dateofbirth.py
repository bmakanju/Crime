# Generated by Django 3.2.6 on 2021-09-29 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210929_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dateofbirth',
            field=models.DateField(null=True),
        ),
    ]