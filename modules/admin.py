from django.contrib import admin
from .models import Profile, WorkExperience, Education #, Documents

# Register your models here.
admin.site.register(Profile)
admin.site.register(WorkExperience)
admin.site.register(Education)
#admin.site.register(Documents)
