from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # /admin/
    path('admin/', admin.site.urls),

    # /
    path('', include('packages.urls', namespace='packages')),

    # /cuos/
    path('cuos/', include('cuos.urls', namespace='cuos')),

    # /accounts/
    path('accounts/', include('accounts.urls', namespace='accounts')),
]
