# Generated by Django 3.2.4 on 2021-06-26 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sikud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provinsi',
            name='id',
            field=models.IntegerField(max_length=2, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='provinsi',
            name='nama',
            field=models.CharField(max_length=255),
        ),
    ]