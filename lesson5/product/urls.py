from django.urls import path
from .views import *
urlpatterns = [
    path('', ApartmentsList.as_view(), name = 'apartments_list'),
    path('apartments_detail/<int:pk>/', ApartmentsDetail.as_view(), name = 'apartments_detail'),
    path('apartments_create/', ApartmentsCreate.as_view(), name = 'apartments_create'),
    path('apartments_update/<int:pk>/', ApartmentsUpdate.as_view(), name = 'apartments_update'),
    path('apartments_delete/<int:pk>/', ApartmentsDelete.as_view(), name = 'apartments_delete')
]