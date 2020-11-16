from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, LoginView

app_name = 'accounts'

urlpatterns = [
    # /accounts/signup/
    path('signup/', views.signup, name='signup'),

    # /accounts/logout/
    path('logout/', LogoutView.as_view(), name='logout'),

    # /accounts/login/
    path('login/', LoginView.as_view(
        template_name='accounts/login.html',
        redirect_authenticated_user=True
    ), name='login'),
]
