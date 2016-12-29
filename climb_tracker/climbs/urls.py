from climbs.views import (LocationViewSet, AreaViewSet, RouteViewSet,
                          SessionViewSet)
from django.conf.urls import include, url
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'locations', LocationViewSet)
router.register(r'areas', AreaViewSet)
router.register(r'routes', RouteViewSet)
router.register(r'sessions', SessionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),

]
