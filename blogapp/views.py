from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Blog

def blog_list(request):
    query = Blog.objects.all()
    data = {
        "query": query,
        "title":"list"
    }
    return render(request, "index.html",data)
    # return HttpResponse('<h1>Hello Manas</h1>')
def blog_detail(request, id=None):
    instance = get_object_or_404(Blog,id=id)
    data = {
        "title":instance.title,
        "instance":instance,
    }
    return render(request, "post_detail.html",data)

def blog_create(request):
    return HttpResponse('<h1>Create Manas</h1>')

def blog_update(request):
    return HttpResponse('<h1>Update Manas</h1>')

def blog_delete(request):
    return HttpResponse('<h1>Delete Manas</h1>')