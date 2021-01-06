from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/Date", {'fields': ["title", "date_published"]}),
        ("Content", {'fields': ["draft", "thumbnail"]})
    ]

    """formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        models.CharField: {'widget': TinyMCE(mce_attrs={'width': 800})}
    }"""
admin.site.register(Post)
admin.site.register(Contactus)
admin.site.register(Comment)
admin.site.register(Ques)
admin.site.register(EReply)


