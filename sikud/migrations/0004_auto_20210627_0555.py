# Generated by Django 3.2.4 on 2021-06-26 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sikud', '0003_desa_kabupaten_kecamatan'),
    ]

    operations = [
        migrations.CreateModel(
            name='JenjangPendidikan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='desa',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='desa',
            name='nama',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='kabupaten',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='kabupaten',
            name='nama',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='kecamatan',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='kecamatan',
            name='nama',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='provinsi',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
