from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Domain)
admin.site.register(Tag)
admin.site.register(UserChoice)
# Register your models here.
