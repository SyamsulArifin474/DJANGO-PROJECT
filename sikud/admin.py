from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from sikud.models import *  # Provinsi, Kabupaten, Kecamatan, Desa


@admin.register(Provinsi)
class ProvinsiAdmin(ImportExportModelAdmin):
    list_display = ("id", "nama")
    pass


@admin.register(Kabupaten)
class KabupatenAdmin(ImportExportModelAdmin):
    list_display = ("id", "provinsi_id", "nama")
    pass


@admin.register(Kecamatan)
class KecamatanAdmin(ImportExportModelAdmin):
    list_display = ("id", "kabupaten_id", "nama")
    pass


@admin.register(Desa)
class DesaAdmin(ImportExportModelAdmin):
    list_display = ("id", "kecamatan_id", "nama")
    pass

# Register your models here.


admin.site.register(JenjangPendidikan)
admin.site.register(Formulir)
