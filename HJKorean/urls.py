from django.conf.urls import patterns, include, url
from django.contrib import admin
from Main.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', main_page, name='main_page'),
    url(r'^korean_black_page/', korean_black_page, name='korean_black_page'),
    url(r'^check_answer/', check_answer, name='check_answer'),


    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
