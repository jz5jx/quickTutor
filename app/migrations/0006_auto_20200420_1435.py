# Generated by Django 3.0.3 on 2020-04-20 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200415_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.CharField(default='New User', max_length=100),
        ),
    ]