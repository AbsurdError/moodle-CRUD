from django.contrib import admin
from .models import Person, Gender
# Register your models here.
admin.site.register(Person)
admin.site.register(Gender)