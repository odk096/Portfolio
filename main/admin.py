from django.contrib import admin
from .models import Previous_work
from .models import profile_pic
from .models import CV
from.models import contact

# Register your models here.

admin.site.register(Previous_work)
admin.site.register(profile_pic)
admin.site.register(CV)
admin.site.register(contact)