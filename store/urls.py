from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views

from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]
