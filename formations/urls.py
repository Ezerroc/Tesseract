from django.urls import path
from . import views

urlpatterns = [
    path('formations/', views.formation, name='formations'),
    path('formations/<int:pdf_id>/pdf', views.pdf_view, name='formation_pdf'),
]
