from django.conf.urls import patterns, include, url
from django.contrib import admin
from Main.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', main_page, name='main_page'),
    url(r'^korean_black_page/(?P<set_id>\d+)/', korean_black_page, name='korean_black_page'),
    url(r'^korean_black_page_wrong/(?P<set_id>\d+)/', korean_black_page_wrong, name='korean_black_page_wrong'),
    url(r'^check_answer/', check_answer, name='check_answer'),
    url(r'^insert_problems/', insert_problems, name='insert_problems'),


    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
