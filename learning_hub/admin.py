from django.contrib import admin
from .models import Users, Questions, Quiz, Topic

admin.site.register(Users)
admin.site.register(Questions)
admin.site.register(Quiz)
admin.site.register(Topic)