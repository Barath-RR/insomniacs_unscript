# Generated by Django 3.2.5 on 2022-01-22 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='mobile',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]