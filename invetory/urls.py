
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from invetory import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('accounts.urls')),
    # path('users/', include('users.urls')),
    path('', include('users.urls')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
