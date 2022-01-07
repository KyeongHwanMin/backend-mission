from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from product.views import ProductListview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListview.as_view(), name='home'),
    # path('', TemplateView.as_view(template_name='base.html'), name='base'),

    path('accounts/', include('accounts.urls')),
    path('product/', include('product.urls')),
    path('comment/', include('comment.urls')),

    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
