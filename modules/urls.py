from django.urls import path
from . import views

urlpatterns=[
    path('education/', views.education, name='education'),
    path('documents/', views.add_documents, name='documents'),
    path('work/', views.work_experience, name='work'),
    # path('profile/', views.profile_user, name="profile-user"),
    path('personal/', views.personal_details, name="personal-details"),
    path('jobs/',views.jobs,name='jobs' ),
    #MODERATOR ONLY URLS
    path('profile/',views.profile, name='profile'),
    #CRUD OPERATIONS
    path('staff/addjob', views.add_Job, name="add_job"), #CREATE
    path('staff/<int:job_id>/', views.job_view, name='job_view' ), #READ
    path('staff/<int:job_id>/update', views.update_job, name='update_job'), #UPDATE
    path('staff/<int:job_id>/delete', views.delete_job, name='delete_job'), #DELETE

]
