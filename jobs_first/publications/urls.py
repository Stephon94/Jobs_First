from django.conf.urls import url
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import views
from jobs_first import settings

urlpatterns = [
    url(r'^$', views.publications_page, name='publications_page'),
url(r'^(?P<slug>[-\w]+)/$', views.publications_article, name='publications_article'),
url(r'^pdf/(?P<filename>.*)$', views.pdf_download),
]
urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
