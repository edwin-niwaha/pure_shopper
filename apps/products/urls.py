# urls.py
from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    # ** Category URLs **
    path("categories/", views.categories_list_view, name="categories_list"),
    path("categories/add/", views.categories_add_view, name="categories_add"),
    path(
        "categories/update/<str:category_id>/",
        views.categories_update_view,
        name="categories_update",
    ),
    path(
        "categories/delete/<str:category_id>/",
        views.categories_delete_view,
        name="categories_delete",
    ),
    # ** Product URLs **
    path("all", views.products_list_all, name="products_list_all"),
    path("", views.products_list_view, name="products_list"),
    path("add/", views.products_add_view, name="products_add"),
    path(
        "update/<str:product_id>/", views.products_update_view, name="products_update"
    ),
    path(
        "delete/<str:product_id>/", views.products_delete_view, name="products_delete"
    ),
    # ** Product Image URLs **
    path("product-image/", views.update_product_image, name="update_product_image"),
    path("product-image/list/", views.product_images, name="product_images"),
    path(
        "product-image/delete/<int:pk>/",
        views.delete_product_image,
        name="delete_product_image",
    ),
    # ** Stock Alerts **
    path("stock-alerts/", views.stock_alerts_view, name="stock_alerts"),
    path("discounted/", views.discounted_product_list_view, name="discounted_products"),
    path("shop-now", views.shop_homepage_view, name="shop_homepage"),
    # Other URL patterns for product details
]
