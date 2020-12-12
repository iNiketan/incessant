from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from .models import Post, Contactus
from .forms import CreateUserForm


# Create your views her
def frontpage(request):
    context = {'post': Post.objects.all}
    return render(request, 'childapp/frontpage.html', context=context)

def aboutapp(request):
    return render(request, 'childapp/about.html')

def contactus(request):
    if request.method == 'POST':
        name = request.POST['name']
        mob = request.POST['mob']
        email = request.POST['email']
        message = request.POST['message']
        contact = Contactus(name=name, mobile=mob, email=email, message=message)
        contact.save()
    return render(request, 'childapp/contactUs.html')

def services(request):
    return render(request, 'childapp/services.html')

def carear(request):
    return render(request, 'childapp/carear.html')

##############################################
def blog(request):
    post = Post.objects.all()
    return render(request, 'childapp/blog.html', context={'post': post})


def single(request, sno):
    details = Post.objects.get(sno=sno)
    return render(request, 'childapp/single.html', {'details':details})
###############################################

##### signup########
def signUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            user = User.objects.create_user(username, email, password1)
            user.save()
            login(request, user)
            messages.success(request,f"new accout created {user.username}")
            messages.info(request, f"You are loged in as {user.username}")
            return redirect('childapp:frontpage')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{form.error_messages[msg]}")

            return render(request=request,
                          template_name="childapp/registration.html",
                          context={"form": form})

    form = UserCreationForm
    return render(request, 'childapp/registration.html', context={'form':form})

def logout_request(request):
    logout(request)
    messages.info(request, "Loged out successfully!!")
    return redirect('childapp:frontpage')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print('form valided')
            loginusername = request.POST['loginusername']
            loginpassword = request.POST['loginpassword']
            user = authenticate(username=loginusername, password=loginpassword)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are loged in as {user.username}")
                return redirect('childapp:frontpage')

            else:
                for msg in form.error_messages:
                    messages.error(request, f"{form.error_messages[msg]}")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{form.error_messages[msg]}")
                print(form.error_messages[msg])
    form = AuthenticationForm()
    return render(request, 'childapp/login.html')




