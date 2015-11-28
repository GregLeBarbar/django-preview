from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from datetime import datetime
from formtools.preview import FormPreview

from news.models import News


class NewsForm(ModelForm):
    
    class Meta:
        model = News
        fields = ['title', 'text']
        
        
class NewsFormPreview(FormPreview):
    
    # Redefine the template
    form_template = 'form.html'
    preview_template = 'preview.html'
    
    def process_preview(self, request, form, context):
        print "processed"
        
    def parse_params(self, *args, **kwargs):
        
        news_id = kwargs['news_id']
        self.state['news_id'] = news_id
        
    def get_initial(self, request):
        """
        Takes a request argument and returns a dictionary to pass to the form's
        ``initial`` kwarg when the form is being created from an HTTP get.
        """
        news = News.objects.get(id=self.state['news_id'])
        
        return {'instance': news,}


    def done(self, request, cleaned_data):
        
        # http://stackoverflow.com/questions/628132/django-form-preview-how-to-work-with-cleaned-data
        #  **cleaned_data 
        # news = News(**{'key':'value',})
        news = News(**cleaned_data)
        news.publish_date = datetime.now()
        news.save()
        
        # Redirect
        url = reverse('news-detail', kwargs={'slug': news.slug})
        return HttpResponseRedirect(url)
    