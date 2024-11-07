from django.shortcuts import render, redirect
from .models import userPost
from .forms import postForm, createAuthforms, CustomPasswordChangeForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

def home(request):
    posts = userPost.objects.all().order_by('-created_at')
    return render(request, 'pages/home.html', {'posts': posts})

def blog(request):
    posts = userPost.objects.all().order_by('-created_at')
    return render(request, 'pages/blog.html', {'posts': posts})

@login_required
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

@login_required
def updatepost(request, pk):
    post = get_object_or_404(userPost, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = postForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('blog')
    else:
        form = postForm(instance=post)
    
    return render(request, 'pages/updatepost.html', {'form': form})

@login_required
def deletepost(request, pk):
    post = get_object_or_404(userPost, pk=pk, user = request.user)
    post.delete()
    return redirect('blog')

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'registration/login.html')


def register(request):
    if request.method == 'POST':
        form = createAuthforms(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('login')
    else:
        form = createAuthforms()
    return render(request, 'registration/register.html', {'form': form})

def profiles(request):
    return render(request, 'registration/profiles.html')

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the home or login page after logout



@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)  # Pass POST data
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Prevents logout after password change
            messages.success(request, 'Your password has been changed successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomPasswordChangeForm(user=request.user)

    return render(request, 'registration/changepassword.html', {'form': form})


