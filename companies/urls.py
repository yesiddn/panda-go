from django.urls import path
from .views import CompanyListCreateView, CompanyRetrieveUpdateDestroyView

urlpatterns = [
    path('companies/', CompanyListCreateView.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', CompanyRetrieveUpdateDestroyView.as_view(), name='company-detail'),
]