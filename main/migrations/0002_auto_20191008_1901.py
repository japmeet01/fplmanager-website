# Generated by Django 2.2.5 on 2019-10-08 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='id',
            field=models.CharField(max_length=3, primary_key=True, serialize=False),
        ),
    ]
