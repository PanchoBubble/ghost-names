from django.urls import path, include
from django.contrib.auth.views import LogoutView
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pick-name', views.PickName.as_view(), name='pick-name'),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view(), name='logout'),
]