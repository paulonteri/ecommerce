from django.urls import path

from accounts.api.addresses import CountryListView, AddressListView, AddressCreateView, AddressUpdateView, \
    AddressDeleteView

urlpatterns = [
    path('countries/', CountryListView.as_view(), name='country-list'),
    path('', AddressListView.as_view(), name='address-list'),
    path('create/', AddressCreateView.as_view(), name='address-create'),
    path('<pk>/update/',
         AddressUpdateView.as_view(), name='address-update'),
    path('<pk>/delete/',
         AddressDeleteView.as_view(), name='address-delete'),

]
