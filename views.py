from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



def index(request):
    return render(request, 'wall_app/index.html')

from .models import User
def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/')

    hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    decoded_hash = hashed.decode('utf-8')

    user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=decoded_hash, birth_year=request.POST['birth_year'])
    print(f" user {user.id}")
    request.session['u_id'] = user.id
    request.session['u_fname'] = user.first_name

    return redirect('/wall')

        
def login(request):
    user_list = User.objects.filter(email=request.POST['email'])
    user = user_list[0]
    print(user.id)

    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        context = {
            'user': user
        }

    
    return render(request, 'wall_app/wall.html')

def wall(request):
    context = {
        'posts' : Message.objects.all(),
    }
    return render(request, 'wall_app/wall.html', context)

def post(request):
    message = Message.objects.create(message=request.POST['message'], messager=User.objects.get(id=request.session['u_id']))
    print(message.id)
    return redirect('/wall')

    
def comment(request):
    comment = Comment.objects.create(comment=request.POST['comment'], commentor=User.objects.get(id=request.session['u_id']), post=Message.objects.get(id=request.POST['post_id']))
    print(comment.id)
    return redirect('/wall')

def logout(request):
    return render(request,"wall_app/logout.html")

def delmsg(request, id):
    Message.objects.get(id=id).delete()
    return redirect('/wall')

def delcom(request, id):
    Comment.objects.get(id=id).delete()
    return redirect('/wall')