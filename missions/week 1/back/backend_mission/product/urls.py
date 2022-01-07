from django.urls import path

from . import views
from product.views import ProductCreateView, ProductDetailView, ProductDeleteView, product_list_view

app_name = 'product'

# breakpoint()
urlpatterns = [
    # path('list/', ProductListview.as_view(), name='list'),
    path('list/', product_list_view, name='list'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),


]