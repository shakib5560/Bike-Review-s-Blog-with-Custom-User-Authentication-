from django.shortcuts import render, redirect
from .models import userPost
from .forms import postForm
from django.shortcuts import get_object_or_404

def home(request):
    posts = userPost.objects.all().order_by('-created_at')
    return render(request, 'pages/home.html', {'posts': posts})

def blog(request):
    posts = userPost.objects.all().order_by('-created_at')
    return render(request, 'pages/blog.html', {'posts': posts})

def createpost(request):
    if request.method == 'POST':
        form = postForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('blog')
    else:
        form = postForm()
    return render(request, 'pages/createpost.html', {'form': form})

def updatepost(request, pk):
    post = get_object_or_404(userPost, pk=pk, user = request.user)
    if request.method == 'POST':
        form = postForm(request.POST, instance=post )
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('blog')
    else:
        form = postForm(instance=post)
    return render(request, 'pages/updatepost.html', {'form': form})

def deletepost(request, pk):
    post = get_object_or_404(userPost, pk=pk, user = request.user)
    post.delete()
    return redirect('blog')

# Create your views here.
