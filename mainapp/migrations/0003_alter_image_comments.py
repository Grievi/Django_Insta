# Generated by Django 3.2.8 on 2021-10-18 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20211018_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='comments',
            field=models.IntegerField(default=0),
        ),
    ]
