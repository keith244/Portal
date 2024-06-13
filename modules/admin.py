from django.contrib import admin
from .models import Profile, WorkExperience, Education

# Register your models here.
admin.site.register(Profile)
admin.site.register(WorkExperience)
admin.site.register(Education)
