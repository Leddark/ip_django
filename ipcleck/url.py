from django.urls import path
from . import views


app_name = 'ipcleck'

urlpatterns = [
    

    path('host', views.ipmy , name = 'ppp'),
    path('', views.index , name = 'in'),
    path('ip', views.yyy , name = 'yy'),
    
]
