"""jobs_first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import views

urlpatterns = [
    url(r'^', include('home_page.urls')),
    url(r'^about/', include('about_us.urls')),
    url(r'^our-work/', include('our_work.urls')),
    url(r'^publication/', include('publications.urls')),
    url(r'^page/', include('generic_page.urls')),
    url(r'^Article/', include('publications.urls')),
    url(r'^media/', include('media.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^email/', views.send_email, name='email'),
]
