from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home-page', views.home, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('mail/', views.success_view, name='mail'),
    path('mail/delete/<int:id>', views.delete, name='delete'),
    path('mail/edit/<int:id>', views.edit, name='edit'),
    path('success/', views.index, name='success'),
]
