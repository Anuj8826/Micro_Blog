from django.conf.urls import patterns, include, url
from article.views import HelloTemplate
#from registration.forms import RegistrationFormUniqueEmail
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('article.urls')),
    url(r'^articles/', include('article.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', 'article.views.hello'),
    url(r'^hello_template/$','article.views.hello_template'),
    url(r'^hello_template_simple/$','article.views.hello_template_simple'),
    url('^hello_class_view/$',HelloTemplate.as_view()),


    url(r'^accounts/login/$', 'django_test.views.login'),
    url(r'^accounts/auth/$', 'django_test.views.auth_view'),
    url(r'^accounts/logout/$', 'django_test.views.logout'),
    url(r'^accounts/loggedin/$', 'django_test.views.loggedin'),
    url(r'^accounts/invalid/$',  'django_test.views.invalid_login'),
    url(r'^accounts/register/$', 'django_test.views.register_user'), 
          
    url(r'^accounts/register_success/$', 'django_test.views.register_success'),
    
    
)
urlpatterns = patterns('',
    
    (r'^map/$', 'article.views.index'),
)