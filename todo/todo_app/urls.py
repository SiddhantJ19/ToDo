from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='todo-home'),
    path('about/',views.about, name='todo-about')
]