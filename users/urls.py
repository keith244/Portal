from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.ilogin,name='users-login'),
    path('register/',views.iregister,name='users-register'),
    # path('',views.index,name='users-index'),
    path('logout/', views.ilogout, name='users-logout'),
    path('forgot/password/', views.forgot_password, name='forgot_password'),
    path('activate/<str:id>/', views.activate_user, name='activate'),
    path('resend/activation/link/', views.resend_activation_link, name='resend_activation_link'),
    path('reset/password/<str:id>', views.reset_password, name='reset_password'),
    path('reset/password/confirm/<str:uidb64>/<str:token>/', views.reset_password_confirm, name='reset_password_confirm'),
    path('reset/password/done/', views.reset_password_done, name='reset_password_done'),
    # Add other URL patterns here if needed
]
