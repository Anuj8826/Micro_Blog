from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'article.views.articles'),
    url(r'^all/$', 'article.views.articles'),
    url(r'get/(?P<article_id>\d+)/$', 'article.views.article'),
    url(r'older/$', 'article.views.older_articles'),
)

