
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from myapp.views import *
route=DefaultRouter()
route.register('data',ScreenShotView,basename='data')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(route.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

