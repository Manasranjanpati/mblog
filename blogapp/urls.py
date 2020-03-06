from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'list', blog_list),
    url(r'create/',blog_create),
    url(r'(?P<id>\d+)/',blog_detail, name='blog_detail'),
    url(r'update/',blog_update),
    url(r'delete/',blog_delete),

    # url(r'^blog/',views.blog_view)
] 