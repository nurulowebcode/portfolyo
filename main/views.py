from django.shortcuts import render, redirect
from .models import *


def index_view(request):
    context = {
        'enterance': Enterance.objects.all().order_by('-id')[:1],
        'about': About.objects.all(),
        'about_me_photo': About_me_photo.objects.all().order_by('-id')[:1],
        'know_me': Know_me.objects.all().order_by('-id')[:3],
        'comment': Comment.objects.all().order_by('-id')[:4],
        'savollar': Savollar.objects.all().order_by('-id')[:5],
        'about_info': About_info.objects.all().order_by('-id')[:4],
        'info': Info.objects.all().order_by('-id')[:4],
        'contact': Contact.objects.last()

    }
    return render(request, 'index.html', context)


def create_message_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Contact.objects.create(
            name=name,
            email=email,
            message=message,
        )
        return redirect('index_urls')





# 1. Projects joylash repasitory ga
# git init
# git add .
# git commit -m "something" 
# git branch -M  main
# git remote origin <reposytiry url>
# git push origin main

# 2.O'zgarishni push qilish
# git add .
# git commit -m "something"
# git push

# 3. O'zgarishni yuklab olish
# git pull
