from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.core.exceptions import PermissionDenied

def index(request):
    if 'user_id' in request.session:
        return redirect('/message/new')
    return render(request, "index.html")
#function:login
#route /login
#method GET/POST
def login(request):
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request,value)
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    return redirect('/message/new')

#function:register
#route /register
#method GET/POST
def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        user = User.objects.register(request.POST)
        request.session['user_id'] = user.id
        return redirect('/message/new')

def logout(request):
    request.session.flush()
    return redirect('/')

#function:new
#route /message/new
#method GET

def messageNew(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
        'messages': Message.objects.all()
        }
    return render(request, 'message.html', context)


#function:new
#route /message/create
#method POST

def messageCreate(request):
    message = Message.objects.create(
        text=request.POST['text'],
        user_id=request.session['user_id'])
    return redirect('/message/new')
    
def messageDelete(request, id):
    message_to_delete = Message.objects.get(id=id)
    if message_to_delete.user.id == request.session['user_id']:
        message_to_delete.delete()
        return redirect('/message/new')
    raise PermissionDenied('User do not have permission to delete this message')
    
def commentCreate(request,id):
    message = Message.objects.get(id=id)
    user = User.objects.get(id=request.session['user_id'])
    Comment.objects.create(text=request.POST['text'], user=user, message=message)
    return redirect('/message/new')

def commentDelete(request, id):
    comment_to_delete = Comment.objects.get(id=id)
    if comment_to_delete.user.id == request.session['user_id']:
        comment_to_delete.delete()
        return redirect('/message/new')
    raise PermissionDenied('User do not have permission to delete this comment')