from django.db import models

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

# ================= FORMULIR =========================


# class Formulir(models.Model):
#     no_kk = models.IntegerField(max_length=20)
#     no_nik = models.IntegerField(max_length=20)
#     nama_lengkap = models.CharField(max_length=100)
#     jenis_kelamin = models.Choices()
#     tempat_lahir = models.CharField(max_length=100)
#     tanggal_lahir = models.DateField(auto_now=False, auto_now_add=False)
#     status_perkawinan
#     jenjang_pendidikan
#     phone1
#     phone2
#     email
#     provinsi
#     kabupaten
#     kecamatan
#     desa
#     wafat
