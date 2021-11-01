from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from users.models import Person
from users.serializers import UserSerializer, PersonSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [DjangoModelPermissions]


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = []
