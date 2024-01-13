from django.urls import path
from blog.views import *

app_name="blog"

urlpatterns = [
    path('', blog_view , name="index"), 
    path('<int:pid>' ,blog_single, name='single' ),
    #path('post-<int:pid>' ,release_post, name='publish' ),
    
    #path('post/<int:pid>/', post_detail, name='post_detail'),
    #path('post-<int:pid>',test,name="test"),
]