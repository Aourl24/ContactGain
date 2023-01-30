from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns=[
	path('admin/',admin.site.urls),
	path('accounts/',include('allauth.account.urls')),
	path('', include('contactgain.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
