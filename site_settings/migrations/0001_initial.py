# Generated by Django 2.1.5 on 2019-01-27 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slogan', models.CharField(blank=True, max_length=50, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='site_logo')),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('google_plus_link', models.URLField(blank=True, null=True)),
                ('rss_link', models.URLField(blank=True, null=True)),
                ('footer_logo', models.ImageField(blank=True, null=True, upload_to='site_logo')),
                ('footer_text', models.TextField(blank=True, null=True)),
                ('copyright', models.CharField(blank=True, max_length=100, null=True)),
                ('header_ad', models.TextField(blank=True, null=True)),
                ('middle_ad', models.TextField(blank=True, null=True)),
                ('footer_ad', models.TextField(blank=True, null=True)),
                ('sidebar_ad', models.TextField(blank=True, null=True)),
            ],
        ),
    ]