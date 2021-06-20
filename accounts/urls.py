from django.urls import path, include
from . import views

urlpatterns = [
    path('admin_home/', views.admin_home, name="admin_home"),

]

