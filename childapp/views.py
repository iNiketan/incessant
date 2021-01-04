from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from django.conf import settings

from .models import Post, Contactus, Ques 
from .forms import CreateUserForm


# Create your views her
def frontpage(request):
    messages.success(request, 'Keep Learning')
    if request.method == 'POST':
        email = request.POST['email']
        que = request.POST['que']
        imgs = request.POST['imgs']
        
        question = Ques(email=email, que=que, img=imgs)
        send_mail('Contact form', message="{} has asked ques {} {}".format(email, que, imgs), from_email=settings.EMAIL_HOST_USER, recipient_list=['sniketan9@gmail.com'], fail_silently=False)
        question.save()

    return render(request, 'childapp/frontpage.html')


def aboutapp(request):
    return render(request, 'childapp/about.html')


def contactus(request):
    if request.method == 'POST':
        name = request.POST['name']
        mob = request.POST['mob']
        email = request.POST['email']
        message = request.POST['message']
        contact = Contactus(name=name, mobile=mob, email=email, message=message)
        send_mail('Contact form', message="{} with mob {} email {} message {}".format(name, mob, email, message), from_email=settings.EMAIL_HOST_USER, recipient_list=['sniketan9@gmail.com','chetansh1104@gmail.com'], fail_silently=False)
        contact.save()
        messages.success(request, "message sent")
    return render(request, 'childapp/contactUs.html')


def services(request):
    return render(request, 'childapp/services.html')


def carear(request):
    return render(request, 'childapp/carear.html')


def blog(request):
    post = Post.objects.all()
    return render(request, 'childapp/blog.html', context={'post': post})


def single(request, post_sno):
    details = Post.objects.get(post_sno=post_sno)
    return render(request, 'childapp/single.html', {'details':details})


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
            # print(messages.success)
            messages.info(request, f"You are loged in as {user.username}")
            return redirect('childapp:frontpage')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{form.error_messages[msg]}")

            return render(request=request,
                          template_name="childapp/signup.html",
                          context={"form": form})

    form = UserCreationForm
    return render(request, 'childapp/signup.html', context={'form':form})


def emailCategories(request):
    return render(request, 'childapp/eCategories.html')

def eContactUs(request):
    cnt = Contactus.objects.all()
    return render(request, 'childapp/eContactUs.html', context={'cnt': cnt})
def eCdetail(request, contact_s_no):
    if request.method == 'POST':
        cuEmail = request.POST['cuEmail']
        cuSub = request.POST['cuSub']
        cuMsg = request.POST['cuMsg']
        send_mail(subject=cuSub, message=cuMsg, from_email=settings.EMAIL_HOST_USER, recipient_list=[cuEmail], fail_silently=False)
        messages.success(request, "message sent")

    edetails = Contactus.objects.get(contact_s_no=contact_s_no)
    return render(request, 'childapp/contactusEmail.html', context={'edetails': edetails})


def logout_request(request):
    logout(request)
    messages.info(request, "Loged out successfully!!")
    return redirect('childapp:frontpage')


def login_request(request):
    if request.method == 'POST':
        #form = AuthenticationForm(data=request.POST)
        #if form.is_valid():
        print('form valided')
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(request, username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are loged in as {user.username}")
            return redirect('childapp:frontpage')

        else:
            form = AuthenticationForm(data=request.POST)
            for msg in form.error_messages:
                messages.error(request, f"{form.error_messages[msg]}")
            return render(request, 'childapp/login.html', {'form': form})

    else:
        form = AuthenticationForm()
        return render(request, 'childapp/login.html',{'form': form})


def login_request2(request):
    if request.method == 'POST':
        #form = AuthenticationForm(data=request.POST)
        #if form.is_valid():
        print('form valided')
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(request, username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are loged in as {user.username}")
            return redirect('childapp:frontpage')

        else:
            form = AuthenticationForm(data=request.POST)
            for msg in form.error_messages:
                messages.error(request, f"{form.error_messages[msg]}")
            return render(request, 'childapp/login2.html', {'form': form})

    else:
        form = AuthenticationForm()
        return render(request, 'childapp/login2.html',{'form': form})


def askque(request):
    return render(request, 'childapp/askque.html')
