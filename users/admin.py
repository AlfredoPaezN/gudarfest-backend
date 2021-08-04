from django.contrib import admin

# Register your models here.
from users.models import Person

admin.site.register(Person)