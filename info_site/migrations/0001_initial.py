# Generated by Django 2.0.13 on 2019-05-14 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('p_number', models.BigIntegerField()),
                ('adress', models.TextField(max_length=100)),
                ('ed_qualifications', models.TextField(max_length=100)),
            ],
        ),
    ]