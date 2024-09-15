from rest_framework.routers import SimpleRouter

from apps.public.views import Weather3hViewSet

router = SimpleRouter()
router.register(r"weather3h", Weather3hViewSet, basename="weather3h")

urlpatterns = [] + router.urls
