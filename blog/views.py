
from django.utils import timezone
from django.http import HttpResponse, HttpResponseNotFound
from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm

from django.core.files.storage import FileSystemStorage

def pdf_view(request):
    fs = FileSystemStorage()
    filename = 'NathanielLowisCVSeptember2020.pdf'
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="NathanielLowisCV.pdf"'
            return response
    else:
        return HttpResponseNotFound('My CV has been misplaced!  I am working hard (hopefully!) sorting out the problem')

def post_list_old_to_new(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list_old.html', {'posts': posts})

def post_list_new_to_old(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list_new.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):

    if request.method == "POST":

        form = PostForm(request.POST)#, request.FILES) 
        print(form)
        if form.is_valid():
            
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        print(form)
    return render(request, 'blog/post_new.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def info_page(request):
    return render(request, 'blog/info_page.html')

def cv_page(request):
    return render(request, 'blog/cv.html')

def home_page(request):
    return render(request, 'blog/homepage.html')

def delete_post(request,post_id=None):
    post_to_delete=Post.objects.get(id=post_id)
    post_to_delete.delete()
    return redirect('post_list_new')

def success(request): 
    return HttpResponse('successfully uploaded') 

def another_success(request):
    return HttpResponse('Another success')