from django.contrib import admin
from .models import WorkExperience, Education, Jobs,Documents, Applications

# Register your models here.
# admin.site.register(Profile)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Jobs)
admin.site.register(Documents)
admin.site.register(Applications)
