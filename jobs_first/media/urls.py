from django.conf.urls import url
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import views
from jobs_first import settings

urlpatterns = [
    url(r'^$', views.news_page, name='news_page'),
    url(r'^(?P<slug>[-\w]+)/$', views.selected_post, name='selected_post' )
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
