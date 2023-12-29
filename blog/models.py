from django.db import models
from django.utils.translation import gettext as _
from blog.abstract import BaseModel
from ckeditor.fields import RichTextField


class BlogFull(BaseModel):
    title = models.CharField(max_length=255, help_text=_("Write title"), verbose_name=_('title'))
    author = models.CharField(max_length=30, help_text=_("Write author"), verbose_name=_("author"))
    image = models.ImageField(upload_to='blog_image/%Y/%m/%d')

    def __str__(self):
        return self.title[:10]

    class Meta:
        verbose_name = _('Blog full')
        verbose_name_plural = _('Blogs full')
