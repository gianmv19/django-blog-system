from django.shortcuts import render

from blogs.models import Category, Blog
from assignments.models import About


def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')

    #Fetch about us
    try:
        about = About.objects.get()
    except:
        about = None
    context = {
        'categories': categories,
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
    }
    return render(request, 'home.html', context)