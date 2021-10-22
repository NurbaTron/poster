"""poster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import TestAPIView, PosterListAPIView, PosterCreateAPIView, PosterRetrieveAPIView, PosterDeleteAPIView, PosterUpdateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('test', test, name='test'),
    # path('test', Test.test_method, name="test"),
    path('test/', TestAPIView.as_view(), name="test"),
    path('', PosterListAPIView.as_view(), name="potser-list"),
    path('create/poster', PosterCreateAPIView.as_view(), name="poster-create"),
    path('poster/<int:pk>', PosterRetrieveAPIView.as_view()),
    path('update/poster/<int:pk>', PosterUpdateAPIView.as_view(), name="update-poster"),
    path('delete/poster/<int:pk>', PosterDeleteAPIView.as_view(), name="delete-poster"),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

