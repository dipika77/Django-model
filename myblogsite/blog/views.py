from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog

def home(request):
    blogs = Blog.objects.all()              #select * from blog
    print(blogs)
    template_name = 'index.html'
    context = {
        'posts': blogs
    }
    return render(request,template_name,context)
def post(request):
    return HttpResponse('post something here')
def post_detail(request):
    return HttpResponse('you can get your post detail here.')


# Create your views here.
