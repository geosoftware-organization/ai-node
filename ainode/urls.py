"""ainode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers
from ainode.views import helloworld

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename=None, base_name=None)

urlpatterns = [
    url(r'^', include(router.urls), kwargs=None, name=None),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^(?P<num1>\d+)/(?P<num2>\d+)/$', helloworld),
    url('admin/', admin.site.urls),
]
