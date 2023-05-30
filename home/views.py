from django.shortcuts import render
from .models import Carousel
from posts.models import Post

def home(request):
    carousels = Carousel.objects.all()
    latest_posts = Post.objects.order_by('-date_posted')[:3]
    return render(request, 'home/home.html', {'carousels': carousels, 'latest_posts': latest_posts})