from django import forms
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from sikud.models import Desa, Formulir, Kabupaten, Kecamatan, Provinsi
from sikud.forms import FormFormulir
# Create your views here.


def loginView(request):
    contex = {
        'title': 'Login | SIAKUD',
    }
    if request.method == "POST":
        username_login = request.POST['inputUsername']
        password_login = request.POST['inputPassword']
        user = authenticate(
            request, username=username_login, password=password_login)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('login')

    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect ('dashboard')
        else:
            return render(request, 'registration/login.html', contex)
    
@login_required(login_url=settings.LOGIN_URL)
def logoutView(request):
    contex = {
        'title': 'Logout | SIAKUD',
    }
    if request.method == "POST":
        if request.POST["logout"] == "Submit":
            logout(request)
            return redirect('login')
    return render(request, 'registration/logout.html', contex)
    
@login_required(login_url=settings.LOGIN_URL)
def index(request):
    context = {
        'title': 'Dashboard | SIAKUD',
        'bc_title': 'Dashboard',

    }
    return render(request, 'dashboard.html',context)

"""<!---------------------------------------- DATA POKOK ----------------------------------------->"""

@login_required(login_url=settings.LOGIN_URL)
def Tambahformulir(request):
    form = FormFormulir()

    context = {
        'form': form,
        'title': 'Formulir | SIAKUD',
        'bc_title': 'Form Formulir',

    }
    return render(request, 'FormFormulir.html', context)

@login_required(login_url=settings.LOGIN_URL)
def formulir(request):
    FormFormulir = Formulir.objects.all()
    Prov = Provinsi.objects.all()
    Kab = Kabupaten.objects.filter(provinsi_id__startswith='')
    Kec = Kecamatan.objects.filter(kabupaten_id__startswith='')
    Des = Desa.objects.filter(desa_id__startswith='')

    context = {
        'FormFormulir': FormFormulir,
        'prov': Prov,
        'kab': Kab,
        'kec': Kec,
        'des': Des,
        'title': 'Formulir | SIAKUD',
        'bc_title': 'Detail Formulir',

    }
    return render(request, 'formulir2.html', context)


"""<!---------------------------------------- DATA POKOK ----------------------------------------->"""

@login_required(login_url=settings.LOGIN_URL)
def biodata(request):
    context = {
        'title': 'Biodata | SIAKUD',
        'bc_title': 'Biodata User',

    }
    return render(request, 'data_pokok/biodata_user.html', context)

@login_required(login_url=settings.LOGIN_URL)
def data_pendapatan(request):
    context = {
        'title': 'Pendapatan | SIAKUD',
        'bc_title': 'Data Pendapatan',

    }
    return render(request, 'data_pokok/data_pendapatan.html', context)

@login_required(login_url=settings.LOGIN_URL)
def data_pengeluaran(request):
    context = {
        'title': 'Data Pengeluaran | SIAKUD',
        'bc_title': 'Data Pengeluaran',

    }
    return render(request, 'data_pokok/data_pengeluaran.html', context)

@login_required(login_url=settings.LOGIN_URL)
def data_perbaikan(request):
    context = {
        'title': 'Data Perbaikan | SIAKUD',
        'bc_title': 'Data Perbaikan',

    }
    return render(request, 'data_pokok/data_perbaikan.html', context)

@login_required(login_url=settings.LOGIN_URL)
def data_unit(request):
    context = {
        'title': 'Unit | SIAKUD',
        'bc_title': 'Data Unit',

    }
    return render(request, 'data_pokok/data_unit.html', context)

@login_required(login_url=settings.LOGIN_URL)
def user(request):
    context = {
        'title': 'User | SIAKUD',
        'bc_title': 'User',

    }
    return render(request, 'data_pokok/user.html', context)


"""<!---------------------------------------- KEPEGAWAIAN ----------------------------------------->"""

@login_required(login_url=settings.LOGIN_URL)
def karyawan(request):
    context = {
        'title': 'Karyawan | SIAKUD',
        'bc_title': 'Karyawan',

    }
    return render(request, 'kepegawaian/karyawan.html', context)

@login_required(login_url=settings.LOGIN_URL)
def presensi(request):
    context = {
        'title': 'Presensi | SIAKUD',
        'bc_title': 'Presensi',

    }
    return render(request, 'kepegawaian/presensi.html', context)
