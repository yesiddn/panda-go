from django.urls import path
from .views import LocalityListView

urlpatterns = [
    path('', LocalityListView.as_view(), name='locality-list'),
]
