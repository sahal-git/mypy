from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('about/', views.about_page_view, name='about')
]