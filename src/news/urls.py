# coding:utf-8
from django.conf.urls import patterns, url

from news.forms import NewsFormPreview, NewsForm
from news.views import NewsDetailView


urlpatterns = patterns('news.views',
                       
    url(r'^create/$', NewsFormPreview(NewsForm), name="create_news"),
    url(r'^edit/(?P<news_id>\d+)/$', NewsFormPreview(NewsForm), name="edit_news"),
    
    url(r'^(?P<slug>[-\w]+)/$', NewsDetailView.as_view(), name='news-detail'),
)