from django.contrib import admin

from .models import UserModel,AdminModel

# Register your models here.
admin.site.register(UserModel)
admin.site.register(AdminModel)