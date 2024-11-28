from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('plants', views.plant_page, name='plant_page'),
    path('plant/<int:plant_id>/<int:micro_id>/', views.plant_view_page, name='plant_view_page'),
    path('details/<int:test_id>/', views.detail_view, name='detail_view'),
    path('compounds/', views.compounds_page, name='compounds_page'),
    path('compounds/<int:compound_id>/<int:micro_id>/', views.compound_records, name='compound_records'),
    path('compounds/record/<int:record_id>/', views.record_detail, name='record_detail'),
    path('extracts/', views.extracts_page, name='extracts_page'),
    path('contact/', views.contact_page, name='contact_page'),
]
