from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.Signup.as_view(), name="signup"),
]
