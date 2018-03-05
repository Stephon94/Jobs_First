from django.conf.urls import url
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import views
from jobs_first import settings
# from Home import views

urlpatterns = [
    url(r'^$', views.about_us_page, name='about_us_page'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
