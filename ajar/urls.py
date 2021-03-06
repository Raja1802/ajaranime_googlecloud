"""ajar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from home.sitemaps import EpisodeSitemap_1,EpisodeSitemap_2,EpisodeSitemap_3, InfoSitemap
from home.feed import AnimeFeed

from django.contrib.sitemaps.views import sitemap
sitemaps_1 = {
    'episodes': EpisodeSitemap_1(),
}
sitemaps_2 = {
    'episodes': EpisodeSitemap_2(),
}
sitemaps_3 = {
    'episodes': EpisodeSitemap_3(),
}
sitemaps_4 = {
    'anime': InfoSitemap(),
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'), ),
    path('anime/', include('anime.urls'), ),
    path('anime/info/', include('info.urls'),),
    path('anime/play/', include('play.urls'),),
    path('schedule/', include('schedule.urls'), ),
    path('sitemap_1.xml', sitemap,{'sitemaps': sitemaps_1}),
    path('sitemap_2.xml', sitemap,{'sitemaps': sitemaps_2}),
    path('sitemap_3.xml', sitemap,{'sitemaps': sitemaps_3}),
    path('sitemap_4.xml', sitemap,{'sitemaps': sitemaps_4}),
    path('robots.txt', include('robots.urls'),),
    path('feed/', AnimeFeed()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'home.views.error_404'
handler403 = 'home.views.error_404'
handler500 = 'home.views.error_500'
handler400 = 'home.views.error_404'
