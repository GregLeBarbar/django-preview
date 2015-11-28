from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.detail import DetailView

from news.forms import NewsForm, NewsFormPreview
from news.models import News


def home(request):
    
    news = News.objects.all()
    
    return render(
        request,
        'home.html',
        {
         'news': news,
         }
    )
    
def edit_news(request, news_id):
    
    
    news = News.objects.get(id=news_id)
    form = NewsForm(instance=news)
    NewsFormPreview(NewsForm)
    url = reverse('create_news',)
    return HttpResponseRedirect(url)
    
    

    
class NewsDetailView(DetailView):
    template_name = 'news_detail.html'
    model = News
