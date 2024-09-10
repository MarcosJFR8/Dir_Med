from django.urls import path
from .views import HomeView

urlpatterns = [
    path('', HomeView_as_view(), name='home'),
]