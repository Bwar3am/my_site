from django.contrib import admin
from blog.models import posts , category , comment
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
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ['name','post','approach','created_date']
    list_filter = ('post','approach')
    search_fields = ['name','post']

admin.site.register(comment,CommentAdmin)
admin.site.register(category)
admin.site.register(posts,postadmin)
