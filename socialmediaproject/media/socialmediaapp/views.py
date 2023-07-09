from django.shortcuts import render,redirect, get_object_or_404
from .models import Post, Profile, Images
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from django.forms import modelformset_factory

def post_list(request):
    posts_list = Post.objects.all().order_by('-id')
    query = request.GET.get('query')
    if query:
        posts = Post.objects.filter(
        Q(title__contains = query) |
        Q(author__username = query) |
        Q(body__contains = query)
        )
    paginator = Paginator(posts_list,4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'post_list.html',{'posts':posts})

def post_detail(request,id,slug):
    post = get_object_or_404(Post, id=id, slug=slug)
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True
    context = {
        'post':post,
        'is_liked':is_liked,
        'total_likes':post.total_likes(),
    }
    return render(request,'post_detail.html',context)

def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(post.get_absolute_url())

def post_create(request):
    ImageFormSet = modelformset_factory(Images, fields=('image',), extra=4)
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        formset = ImageFormSet(request.POST or None, request.FILES or None)

        if form.is_valid() and formset.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            for i in formset:
                try:
                    photo = Images(post=post, image=i.cleaned_data['image'])
                    photo.save()
                except Exception:
                    break
            return redirect('/post_list')

    else:
        form = PostCreateForm()
        formset = ImageFormSet(queryset=Images.objects.none())
        return render(request,'post_create.html',{'form':form,'formset':formset})


@receiver(pre_save, sender=Post)
def pre_save_slug(sender, **kwargs):
    slug = slugify(kwargs['instance'].title)
    kwargs['instance'].slug = slug

def user_logout(request):
    logout(request)
    return redirect('/post_list')

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username1 = request.POST['username']
            password1 = request.POST['password']
            user = authenticate(username=username1, password=password1)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('/post_list')
                else:
                    return HttpResponse("User is not active")
            else:
                return HttpResponse("User is None")
    else:
        form = UserLoginForm()
        return render(request, 'login.html',{'form':form})

def user_register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
                                                                                                             #Profile.objects.create(user=new_user)
            return redirect('/post_list')
    else:
        form = UserRegistrationForm()
        return render(request, 'register.html',{'form':form})


def edit_profile(request):
    if request.method == "POST":
        user_form = UserEditForm(data=request.POST or None, instance=request.user)
        profile_form = ProfileEditForm(data=request.POST or None, instance=request.user.profile, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/post_list')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request, 'edit_profile.html',{'user_form':user_form, 'profile_form':profile_form})

def post_edit(request,id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostEditForm(request.POST or None, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = PostEditForm(instance=post)
        return render(request, 'post_edit.html',{'form':form})


def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('post_list')

