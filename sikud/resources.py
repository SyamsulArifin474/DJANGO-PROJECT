from import_export import resources
from sikud.models import Provinsi, Kabupaten, Kecamatan, Desa


class ProvinsiResources(resources.ModelResource):
    class Meta:
        model = Provinsi


class KabupatenResources(resources.ModelResource):
    class Meta:
        model = Kabupaten


class KecamatanResources(resources.ModelResource):
    class Meta:
        model = Kecamatan


class DesaResources(resources.ModelResource):
    class Meta:
        model = Desa
