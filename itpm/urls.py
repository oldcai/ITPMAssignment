"""itpm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views.generic import TemplateView

from loyalty_program.views import ApplyOfferView, HomepageView, OfferDetailView, ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomepageView.as_view(), name='home'),
    path('profile/', login_required(ProfileView.as_view()), name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path(f'offer/<pk>', login_required(OfferDetailView.as_view()), name='offer-detail-view'),
    path(f'apply-offer/', login_required(ApplyOfferView.as_view()), name='apply-offer-view'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('coupons/', TemplateView.as_view(template_name='coupons.html'), name='coupons'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
