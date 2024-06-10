from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('contact/page/<int:id>/', views.contact, name = 'contact'),

]