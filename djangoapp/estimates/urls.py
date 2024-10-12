from django.urls import path

from djangoapp.estimates.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]