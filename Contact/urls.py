from django.urls import path
from Contact import views
app_name = 'Contact'

urlpatterns = [
    path('', views.contact, name="contact"),   
]