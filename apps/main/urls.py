from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='users-home'),
    # path("dashboard/", views.dashboard, name="dashboard"),
]
