# Generated by Django 2.1.5 on 2019-01-21 18:55

from django.db import migrations, models
import user_profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0002_auto_20190118_0054'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('objects', user_profiles.models.UserProfileManager()),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='biography',
            field=models.TextField(blank=True, null=True),
        ),
    ]
