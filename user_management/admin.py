from django.contrib import admin

# Register your models here.
from user_management import models


admin.site.register(models.UserProfile)