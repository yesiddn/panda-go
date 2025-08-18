from django.urls import path
from .views import WasteCategoryListView

urlpatterns = [
    path('', WasteCategoryListView.as_view(), name='wastecategory-list'),
]
