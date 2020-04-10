from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Blog
from .forms import BlogForm
from django.contrib import messages


def blog_list(request):
    query = Blog.objects.all()
    data = {
        "query": query,
        "title": "list"
    }
    return render(request, "index.html", data)
    # return HttpResponse('<h1>Hello Manas</h1>')


def blog_detail(request, id=None):
    instance = get_object_or_404(Blog, id=id)
    data = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "post_detail.html", data)


def blog_create(request):
    form = BlogForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Successfully post created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form
    }
    return render(request, "post_create.html", context)


def blog_update(request, id=None):
    instance = get_object_or_404(Blog, id=id)
    form = BlogForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

        context = {
            "title": instance.title,
            "instance": instance,
            "form": form,
        }
    return render(request, "post_create.html", context)


def blog_delete(request):
    return HttpResponse('<h1>Delete Manas</h1>')
