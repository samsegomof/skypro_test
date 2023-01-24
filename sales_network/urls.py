from django.urls import path

from . import views

urlpatterns = [
    path("participant/create", views.ParticipantCreateView.as_view(), name='create_participant'),
    path("participant/list", views.ParticipantListView.as_view(), name='list_participants'),
    path("participant/<pk>", views.ParticipantView.as_view(), name='retrieve_participant'),
    path("supplier/create", views.SupplierCreateView.as_view(), name='create_supplier'),
    path("supplier/list", views.SupplierListView.as_view(), name='list_suppliers'),
    path("supplier/<pk>", views.SupplierView.as_view(), name='retrieve_supplier'),
]
