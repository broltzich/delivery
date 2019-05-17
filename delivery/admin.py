from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Client)
admin.site.register(Worker)
admin.site.register(Post)
admin.site.register(Vehicle)
admin.site.register(Trip)
admin.site.register(Package)
admin.site.register(Profile)

