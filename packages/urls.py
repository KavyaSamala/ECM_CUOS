from django.urls import path
from . import views

app_name = 'packages'

urlpatterns = [
    # /
    path('', views.index, name='index'),

    # /packages/1/
    path('packages/<int:pk>/', views.package, name='package'),

]
