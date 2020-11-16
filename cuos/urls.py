from django.urls import path
from .import views

app_name = 'cuos'

urlpatterns = [

     # /cuos

    path('', views.cuos, name='cuos_url'),

    # /cuos/1/

    path('<int:pk>/', views.cuos_main, name='cuos_url1'),

]