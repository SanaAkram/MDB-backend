from .views import RegisterAPI, KavprofAPI
from knox import views as knox_views
from .views import LoginAPI
from django.urls import path

urlpatterns = [
    path('Kavtech/register/', RegisterAPI.as_view(), name='register'),
    path('Kavtech/login/', LoginAPI.as_view(), name='login'),
    path('Kavtech/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('Kavtech/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('Kavtech/kavprof/', KavprofAPI.as_view(), name='kavprof'),
]
