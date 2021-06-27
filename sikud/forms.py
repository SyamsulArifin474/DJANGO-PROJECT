from django.forms import ModelForm
from sikud.models import Formulir


class FormFormulir(ModelForm):
    class meta:
        model = Formulir
        fields = ['nama_lengkap']  # '__All__'
