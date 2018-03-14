from django.conf.urls import url
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from views import *
import views
from jobs_first import settings
# from Home import views

urlpatterns = [
    url(r'^$', views.our_work_page, name='our_work_page'),
    url(r'/location-api$', views.PartnersJsonEndpoint, name='our_work_api_page'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
