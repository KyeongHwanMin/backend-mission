from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views


urlpatterns = [
  path('admin/', admin.site.urls),
  path('accounts/', include('account.urls')),
  path('', TemplateView.as_view(template_name='base.html'), name='base'),

  path('product/', include('product.urls')),
  path('comment/', include('comment.urls')),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
