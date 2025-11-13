from django.urls import path
from . import views

app_name = 'webapp'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('customers/', views.customers_view, name='customers'),
    path('document-tracking/', views.document_tracking_view, name='document_tracking'),
    path('existing-data/', views.existing_data_view, name='existing_data'),
    path('add-data/', views.add_data_view, name='add_data'),
    path('existing-data/customer-detail/', views.customer_detail_view, name='customer_detail'),
    path('sale-form/', views.sale_form_view, name='sale_form'),
    path('not-interested/', views.not_interested_view, name='not_interested'),
    # API
    path('api/customers/', views.CustomerListCreateView.as_view(), name='api_customers'),
    path('api/customers/<int:pk>/', views.CustomerRetrieveUpdateDestroyView.as_view(), name='api_customer_detail'),
]
