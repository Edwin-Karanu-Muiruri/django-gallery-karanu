# Generated by Django 3.0 on 2020-05-25 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]