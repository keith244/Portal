from django.urls import path
from . import views

urlpatterns=[
    path('education', views.education, name='education'),
    path('modules/documents', views.add_documents, name='documents'),
    path('modules/work', views.work_experience, name="work"),
    path('modules/profile', views.profile_user, name="profile-user"),
    path('faqs/',views.faqs,name='modules-faqs'),
    path('modules/personal', views.personal_details, name="personal-details"),
    path('modules/jobs',views.jobs,name='jobs' ),
    #ADMIN ONLY 
    path('staff/addjob', views.add_Job, name="add_job"),
    path('staff/<int:job_id>/update', views.update_job, name='update_job'), #UPDATE
    path('staff/<int:job_id>/delete', views.delete_job, name='delete_job'), #DELETE

]