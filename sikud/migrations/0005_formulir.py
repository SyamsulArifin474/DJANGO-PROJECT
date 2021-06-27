# Generated by Django 3.2.4 on 2021-06-26 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sikud', '0004_auto_20210627_0555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formulir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_kk', models.IntegerField(null=True)),
                ('no_nik', models.IntegerField(null=True)),
                ('nama_lengkap', models.CharField(max_length=100)),
                ('jenis_kelamin', models.CharField(choices=[('L', 'Laki-Laki'), ('P', 'Perempuan'), ('T', 'Transgender')], default='L', max_length=20)),
                ('tempat_lahir', models.CharField(max_length=100)),
                ('tanggal_lahir', models.DateField()),
                ('status_perkawinan', models.CharField(choices=[('L', 'Lajang'), ('M', 'Menikah')], default='L', max_length=20)),
                ('phone1', models.CharField(max_length=20)),
                ('phone2', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('wafat', models.CharField(choices=[('T', 'TIDAK'), ('Y', 'IYA')], default='T', max_length=20)),
                ('desa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sikud.desa')),
                ('jenjang_pendidikan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sikud.jenjangpendidikan')),
                ('kabupaten', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sikud.kabupaten')),
                ('kecamatan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sikud.kecamatan')),
                ('provinsi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sikud.provinsi')),
            ],
        ),
    ]
