from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import Context
from django.views.generic.base import TemplateView
from article.models import Article
from datetime import timedelta
import datetime
from django.db.models import Q
from django import forms
from django.shortcuts import render_to_response
from gmapi import maps
from gmapi.forms.widgets import GoogleMap 

# Create your views here.
  
def hello(request):
    name = "Anuj"
    html = '<html><body>Hi %s, this seems to have workd!</body></html>'% name
    return HttpResponse(html)

def hello_template(request):
     name ="anuj"
     t = get_template('hello.html')
     html = t.render(Context({'name':name}))
     return HttpResponse(html)

def hello_template_simple(request):
    name="anuj1"
    return render(request,'hello.html',{'name': name})

class HelloTemplate(TemplateView):
   
    template_name = 'hello_class.html'
  
    def get_context_data(self, **kwargs):
        context = super(HelloTemplate,self),get_context_data(**kwargs)
        context['name'] = 'anuj'
        return context

def articles(request):
    now = datetime.datetime.now()
    start_date = now - timedelta(days=1)
    return render(request,'articles.html', {'articles': Article.objects.filter(pub_date__gt= start_date) })  
    


def article(request, article_id=1):
       
    return render(request,'article.html',{'article':Article.objects.get(id=article_id) })


def older_articles(request):
   
    return render(request,'articles.html',{'articles':Article.objects.all() })


class MapForm(forms.Form):
    map = forms.Field(widget=GoogleMap(attrs={'width':510, 'height':510}))


def index(request):
    gmap = maps.Map(opts = {
        'center': maps.LatLng(28.55294, 77.33675),
        'mapTypeId': maps.MapTypeId.ROADMAP,
        'zoom': 3,
        'mapTypeControlOptions': {
             'style': maps.MapTypeControlStyle.DROPDOWN_MENU
        },
    })
    marker = maps.Marker(opts = {
        'map': gmap,
        'position': maps.LatLng(28.55294, 77.33675),
    })
    maps.event.addListener(marker, 'mouseover', 'myobj.markerOver')
    maps.event.addListener(marker, 'mouseout', 'myobj.markerOut')
    info = maps.InfoWindow({
        'content': 'Hello!',
        'disableAutoPan': True
    })
    info.open(gmap, marker)

    context = {'form': MapForm(initial={'map': gmap})}
    return render_to_response('index.html', context)







