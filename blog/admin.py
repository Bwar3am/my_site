from django.contrib import admin
from blog.models import posts , category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
#@admin.register(posts)
class postadmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ['title','id','counted_views','author','counted_views','published_date','created_date','updated_date']
    list_filter = ('status','author')
    ordering=['created_date']
    summernote_fields = ('content',)
    

admin.site.register(category)
admin.site.register(posts,postadmin)