from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from order import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cart/', include(('cart.urls', 'cart'), namespace='cart')),
    url(r'^orders/', include(('order.urls', 'order'), namespace='orders')),
    url(r'^coupons/', include(('coupons.urls', 'coupons'), namespace='coupons')),
    url(r'^', include(('shop.urls', 'shop'), namespace='shop')),
    url(r'^admin/order/(?P<order_id>\d+)/$', views.admin_order_detail, name='admin_order_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)