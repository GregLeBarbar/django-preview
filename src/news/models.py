from autoslug.fields import AutoSlugField
from django.db import models
from django.utils.translation import ugettext_lazy as _


class News(models.Model):
    
    title = models.CharField(verbose_name=_("Title"), max_length=100)
    text = models.TextField(verbose_name=_("Text"), blank=True)
    publish_date = models.DateTimeField(null=True, blank=True)
    slug = AutoSlugField(populate_from='title', unique_with='publish_date')
    
    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')
        db_table = 'news'
        
    def __unicode__(self): 
        return self.title
    
    