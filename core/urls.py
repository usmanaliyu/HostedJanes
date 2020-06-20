from django.urls import path

from . import views
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    ShopView,
    Search,
    CategoryView,
    AboutView,
    ContactView,
    UserView,
    PaystackView,
    paysuccess,
    ContactSuccess,
    terms,
    faq,
    privacy,
)

app_name = 'core'

urlpatterns = [
    path('', HomeView, name='home'),
    path('shop/', ShopView, name='shop'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('search/', Search, name='search'),
    path('category/<slug>/', CategoryView, name='categoryview'),
    path('about/', AboutView, name='about'),
    path('contact/', ContactView, name='contact'),
    path('user/', UserView, name='user'),
    path('janepay/', PaystackView.as_view(), name='janepay'),
    path('paystack-success/', views.paysuccess, name='paystack-success'),
    path('contact-success/', views.ContactSuccess, name='contact-success'),
    path('terms-and-conditions/', views.terms, name='terms'),
    path('faq/', views.faq, name='faq'),
    path('privacy-policy/', views.privacy, name='privacy'),
    path('returns-and-exchange/', views.returns, name='returns'),
    path('shipping-info/', views.shippinginfo, name='shippinginfo'),


]
