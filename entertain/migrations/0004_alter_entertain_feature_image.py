# Generated by Django 3.2.6 on 2021-10-06 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertain', '0003_alter_entertain_feature_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entertain',
            name='feature_image',
            field=models.FileField(default='', upload_to='Entertain'),
        ),
    ]
