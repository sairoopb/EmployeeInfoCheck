# Generated by Django 2.0.13 on 2019-05-14 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='p_number',
            field=models.BigIntegerField(unique=True),
        ),
    ]
