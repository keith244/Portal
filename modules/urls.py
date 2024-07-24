from django.urls import path
from . import views

urlpatterns=[
    path('education/', views.education, name='education'),
    path('documents/', views.add_documents, name='documents'),
    path('work/', views.work_experience, name='work'),
    path('personal/', views.personal_details, name="personal-details"),
    path('jobs/',views.jobs,name='jobs' ),
    path('staff/addjob', views.add_Job, name="add_job"), #CREATE
    path('staff/<int:job_id>/', views.job_details, name='job_details' ), #READ
    path('staff/<int:job_id>/update', views.update_job, name='update_job'), #UPDATE
    path('staff/<int:job_id>/delete', views.delete_job, name='delete_job'), #DELETE

    path('staff/applications/', views.job_applications, name='applications'),
    path('staff/view_applications/', views.view_applications, name='view_applications'),
    path('staff/view_applications/<int:job_id>', views.view_applications, name='view_job_applied'),

    path('jobs_2/', views.jobs_2, name='jobs_2'),

]
