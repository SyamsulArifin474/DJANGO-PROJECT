from django.db import models
from django.utils.translation import deactivate

# Create your models here.


class Provinsi(models.Model):
    id = models.IntegerField(primary_key=True)
    nama = models.CharField(max_length=255)

    def __str__(self):
        return self.nama


class Kabupaten(models.Model):
    id = models.IntegerField(primary_key=True)
    provinsi_id = models.ForeignKey(
        Provinsi, on_delete=models.CASCADE, null=True)
    nama = models.CharField(max_length=255)

    def __str__(self):
        return self.nama


class Kecamatan(models.Model):
    id = models.BigIntegerField(primary_key=True)
    kabupaten_id = models.ForeignKey(
        Kabupaten, on_delete=models.CASCADE, null=True)
    nama = models.CharField(max_length=255)

    def __str__(self):
        return self.nama


class Desa(models.Model):
    id = models.IntegerField(primary_key=True)
    kecamatan_id = models.ForeignKey(
        Kecamatan, on_delete=models.CASCADE, null=True)
    nama = models.CharField(max_length=255)

    def __str__(self):
        return self.nama
# ======================== JENJANG PENDIDIKAN =========================


class JenjangPendidikan(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

# ================= FORMULIR =========================


class Formulir(models.Model):
    no_kk = models.IntegerField(null=True)
    no_nik = models.IntegerField(null=True)
    nama_lengkap = models.CharField(max_length=100)
    j_kelamin = ("L", "Laki-Laki"), ("P", "Perempuan"), ("T", "Transgender")
    jenis_kelamin = models.CharField(
        max_length=20, choices=j_kelamin, default='L')
    tempat_lahir = models.CharField(max_length=100)
    tanggal_lahir = models.DateField(auto_now=False, auto_now_add=False)
    sts_menikah = ("L", "Lajang"), ("M", "Menikah")
    status_perkawinan = models.CharField(
        max_length=20, choices=sts_menikah, default='L')
    jenjang_pendidikan = models.ForeignKey(
        JenjangPendidikan, on_delete=models.CASCADE, null=True)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    provinsi = models.ForeignKey(Provinsi, on_delete=models.CASCADE, null=True)
    prov_id = provinsi
    kabupaten = models.ForeignKey(
        Kabupaten, f, on_delete=models.CASCADE, null=True)
    kecamatan = models.ForeignKey(
        Kecamatan, on_delete=models.CASCADE, null=True)
    desa = models.ForeignKey(Desa, on_delete=models.CASCADE, null=True)
    mati = ("T", "TIDAK"), ("Y", "IYA")
    wafat = models.CharField(max_length=20, choices=mati, default='T')
