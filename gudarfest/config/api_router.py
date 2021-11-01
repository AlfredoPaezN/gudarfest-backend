from rest_framework import routers

from users.viewsets import UserViewSet, PersonViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'people', PersonViewSet)
