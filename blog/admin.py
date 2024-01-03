from django.contrib import admin
from blog.models import posts

# Register your models here.
#@admin.register(posts)
class postadmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ['title','counted_views','counted_views','published_date','created_date','updated_date']
    list_filter = ('status',)
    ordering=['created_date']
    


admin.site.register(posts,postadmin)