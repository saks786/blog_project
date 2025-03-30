from django.shortcuts import render
import requests

def blog_list(request):
    response = requests.get("https://api.sampleapis.com/futurama/episodes")
    blogs = response.json() if response.status_code == 200 else []
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    response = requests.get(f"https://api.sampleapis.com/futurama/episodes/{blog_id}")
    blog = response.json() if response.status_code == 200 else None
    return render(request, 'blog/blog_detail.html', {'blog': blog})

