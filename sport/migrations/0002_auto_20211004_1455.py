# Generated by Django 3.2.6 on 2021-10-04 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SportCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=9999999, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='seply',
            name='commenties',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sport.somment'),
        ),
        migrations.AlterField(
            model_name='somment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sport.sport', to_field='slug'),
        ),
        migrations.AddField(
            model_name='sport',
            name='category',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='sport.sportcategory'),
        ),
    ]
