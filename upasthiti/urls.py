from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.views.generic import RedirectView

urlpatterns = patterns('',
    # Examples:
    url(r'^login/', 'django.contrib.auth.views.login',{'template_name':'login.html'}),
    url(r'^attendance/', include('attendance.urls')),
    url(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'images/favicon.ico')),
    url(r'^admin/', include(admin.site.urls)),

) + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
