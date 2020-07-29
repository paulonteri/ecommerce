from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  #
                  path('products/', include('products.urls')),
                  path('admin/', admin.site.urls),
                  # API URLs
                  path('api/v1/auth/', include('accounts.urls')),
                  path('api/v1/payments/', include('payments.urls')),
                  path('api/v1/products/', include('products.api_urls')),
                  path('api/v1/orders/', include('orders.urls')),
                  path('api/v1/addresses/', include('accounts.address_urls')),
                  #
                  path('', include('frontend.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
