# Generated by Django 2.1.5 on 2019-01-21 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_visited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='visited',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
