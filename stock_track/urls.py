from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.main.urls')),
    path('store/', include('apps.store.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('transactions/', include('apps.transactions.urls')),
    path('invoice/', include('apps.invoice.urls')),
    path('bills/', include('apps.bills.urls'))
]
