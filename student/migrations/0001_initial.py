# Generated by Django 3.2.5 on 2022-01-22 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('teacher_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=50)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('is_mobile_verified', models.BooleanField(default=False)),
                ('first_login', models.DateTimeField(auto_now=True)),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
    ]