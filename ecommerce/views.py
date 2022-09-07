from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import CustomUser, PhoneModel
from .forms import UserRegister,CodeForm
from django.contrib.auth.forms import AuthenticationForm
from .utils import send_sms
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.views.generic import ListView,DetailView
def hello(request):
    return render(request,"home.html")

# Registering User
def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = UserRegister()
    return render(request, "register.html", {'form':form})


#first authenticate user if user exist store its primary key in session and redirect to verify otp view
def login_with_otp(request):
    form = AuthenticationForm()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)        #authenticate user from the data passed in form
        if user is not None:
            request.session['pk'] = user.pk
            return redirect('verify')
    return render(request,'login.html',{'form':form})



"""""
This view will send the otp to user to it's register email address and phone number and 
if user enter correct otp then only he wil be logged in
"""
def verify_otp(request):
    form = CodeForm(request.POST or None)
    pk = request.session['pk']
    if pk:
        user = CustomUser.objects.get(pk=pk)
        code = user.code
        code_user = f"{code}"
        if not request.POST:                            #send otp if it is not POST request
            send_mail(subject="Verification Code",
                      message=f"Your login verification code is {code_user}",
                      from_email="contact@myapp.com",
                      recipient_list=[user.email])

            send_sms(code_user,user.phone)

        if form.is_valid():                                 # validate the otp entered by user
            num = form.cleaned_data.get("otp")

            if str(code) == num:                               # if otp entered by user and generated otp is equal then login the user
                code.save()
                login(request,user)
                return redirect("all-product")
            else:
                return redirect('login')                        # else return to Login page
    return render(request,"otp.html",{'form':form})



class ProductListView(LoginRequiredMixin,ListView):             #loginrequiredmixin to provide access to only logged in user
    model = PhoneModel
    template_name = 'product.html'
    context_object_name = 'products'


class ProductDetailView(DetailView,LoginRequiredMixin):             #loginrequiredmixin to provide access to only logged in user
    model = PhoneModel
    template_name = 'product_detail.html'
    context_object_name = 'product'


def log_out(request):               #logout view

    logout(request)
    return redirect("home")



