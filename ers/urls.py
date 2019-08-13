from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('time', views.get_current_time, name='time'),
    path('report', views.register_error_log, name='report'),
    path('reports', views.register_error_logs, name='reports'),
]