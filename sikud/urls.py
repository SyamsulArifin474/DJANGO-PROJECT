from django.urls import path
from . import views

urlpatterns = [

    path('Formulir/', views.formulir, name='formulir'),
    path('Dashboard/', views.index, name='dashboard'),
    path('Formulir/', views.formulir, name='formulir'),
    # """<!---------------------------------------- DATA POKOK ----------------------------------------->"""
    path('Biodata/', views.biodata, name='biodata'),
    path('DataPokok/Unit/', views.data_unit, name='unit'),
    path('DataPokok/Pendapatan/', views.data_pendapatan, name='pendapatan'),
    path('DataPokok/Pengeluaran/', views.data_pengeluaran, name='pengeluaran'),
    path('DataPokok/Perbaikan/', views.data_perbaikan, name='perbaikan'),
    path('User/', views.user, name='user'),
    # """<!---------------------------------------- KEPEGAWAIAN ----------------------------------------->"""
    path('Kepegawaian/Karyawan/', views.karyawan, name='karyawan'),
    path('Kepegawaian/Presensi/', views.presensi, name='presensi'),

    # path('dashboard/', views.dashboard, name='dashboard'),
    # path('starter/', views.starter, name='starter'),
    # path('Dashboard/Content', views.content, name='content'),
]