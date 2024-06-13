from django.urls import path
from . import views

urlpatterns=[
    path('modules/education', views.education, name='education'),
    path('modules/documents', views.add_documents, name='documents'),
    path('modules/work', views.work_experience, name='work'),
    path('modules/profile', views.profile_user, name="profile-user"),
    path('modules/personal', views.personal_details, name="personal-details"),

    #MODERATOR ONLY URLS
    path('staff/addjob', views.add_Job, name="add_job"),

]