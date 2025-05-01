# urls.py
from django.urls import path
from . import views

app_name = "supplier"
urlpatterns = [
    path("", views.supplier_list, name="supplier_list"),
    path("add/", views.supplier_add, name="supplier_add"),
    path("update/<int:supplier_id>/", views.supplier_update, name="supplier_update"),
    path("delete/<int:supplier_id>/", views.supplier_delete, name="supplier_delete"),
    path('purchase-orders-list/', views.purchase_orders_list, name='purchase-orders-list'),
    path('purchase-orders/add/', views.purchase_order_add, name='purchase_order_create'),
    path('purchase-orders/update/<int:purchase_order_id>/', views.purchase_order_update, name='purchase-order-update'),
    path('purchase-orders/delete/<int:purchase_order_id>/', views.purchase_order_delete, name='purchase-order-delete'),
    path('purchase-order/<int:pk>/', views.purchase_order_detail, name='purchase-order-detail'),
]
