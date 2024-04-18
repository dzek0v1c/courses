from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('auth/', views.auth, name="auth"),
    path('profile/', views.profile, name="profile"),
    path('auth/register', views.register, name="register"),
    path('auth/login', views.login, name="login"),
    path('course1/', views.course1, name="course1"),
    path('course2/', views.course2, name="course2"),
    path('course3/', views.course3, name="course3"),
    path('course4/', views.course4, name="course4"),
    path('course5/', views.course5, name="course5"),
    path('course6/', views.course6, name="course6")
]