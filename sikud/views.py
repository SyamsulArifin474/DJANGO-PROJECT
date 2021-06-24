from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


""" def content(request):
    context = {
        'title': 'Dashboard | SIAKUD',

    }
    return render(request, 'content.html', context) """


def index(request):
    context = {
        'title': 'Dashboard | SIAKUD',
        'bc_title': 'Dashboard',

    }
    return render(request, 'dashboard.html', context)


def formulir(request):
    context = {
        'title': 'Formulir | SIAKUD',
        'bc_title': 'Formulir',

    }
    return render(request, 'formulir.html', context)


"""<!---------------------------------------- DATA POKOK ----------------------------------------->"""


def biodata(request):
    context = {
        'title': 'Biodata | SIAKUD',
        'bc_title': 'Biodata User',

    }
    return render(request, 'data_pokok/biodata_user.html', context)


def data_pendapatan(request):
    context = {
        'title': 'Pendapatan | SIAKUD',
        'bc_title': 'Data Pendapatan',

    }
    return render(request, 'data_pokok/data_pendapatan.html', context)


def data_pengeluaran(request):
    context = {
        'title': 'Data Pengeluaran | SIAKUD',
        'bc_title': 'Data Pengeluaran',

    }
    return render(request, 'data_pokok/data_pengeluaran.html', context)


def data_perbaikan(request):
    context = {
        'title': 'Data Perbaikan | SIAKUD',
        'bc_title': 'Data Perbaikan',

    }
    return render(request, 'data_pokok/data_perbaikan.html', context)


def data_unit(request):
    context = {
        'title': 'Unit | SIAKUD',
        'bc_title': 'Data Unit',

    }
    return render(request, 'data_pokok/data_unit.html', context)


def user(request):
    context = {
        'title': 'User | SIAKUD',
        'bc_title': 'User',

    }
    return render(request, 'data_pokok/user.html', context)


"""<!---------------------------------------- KEPEGAWAIAN ----------------------------------------->"""


def karyawan(request):
    context = {
        'title': 'Karyawan | SIAKUD',
        'bc_title': 'Karyawan',

    }
    return render(request, 'kepegawaian/karyawan.html', context)


def presensi(request):
    context = {
        'title': 'Presensi | SIAKUD',
        'bc_title': 'Presensi',

    }
    return render(request, 'kepegawaian/presensi.html', context)
