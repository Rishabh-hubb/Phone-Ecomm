from django.contrib import admin
from .models import CustomUser,Code,PhoneModel
# Register your models here.

from .forms import *




admin.site.register(Code)
admin.site.register(CustomUser)
admin.site.register(PhoneModel)