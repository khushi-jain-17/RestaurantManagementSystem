from django.urls import path 
from .views import GoogleSocialAuthView
from . import views 

app_name = 'social_auth'

urlpatterns=[
    path("google/", GoogleSocialAuthView.as_view()),
    path("",views.home),
    path("logout",views.logout_view)
]

