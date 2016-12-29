from climbs.views import LocationViewSet
from django.conf.urls import include, url
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'locations', LocationViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),

]
