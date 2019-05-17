from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from .forms import DeliveryRegForm, SignUpForm, AuthForm, EditUserForm
import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login as login_user, logout
from django.contrib.auth.hashers import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django import forms
from .models import Package

# Create your views here.


def index(request):
    return render(request, 'base.html')


def about(request):
    return render(request, 'aboutPage.html')


def activity(request):
    return render(request, 'ourActivityPage.html')


def news(request):
    return render(request, 'newsPage.html')


def vacancy(request):
    return render(request, 'vacancyPage.html')


def partner(request):
    return render(request, 'partnerPage.html')


def service(request):
    return render(request, 'servicePage.html')


def delivery(request):
    if request.method == "POST":
        form = DeliveryRegForm(request.POST)
        if form.is_valid():
            package = form.save(commit=False)
            package.ship_date = datetime.datetime.now()
            if request.user.is_authenticated:
                package.pk_user = request.user
            package.save()
            return render(request, 'successPage.html', {})
    else:
        form = DeliveryRegForm()
    return render(request, 'deliveryPage.html', {'form': form})


def success(request):
    return render(request, 'successPage.html', {})


def sign_up(request):
    names_dict = {}
    errors = []
    form = SignUpForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        names_list = ["username", "password", "email"]
        names_dict = {x: request.POST.get(x, "") for x in names_list}

        try:
            User.objects.get(email=data['email'])
            errors.append('this email is already registered')
        except User.DoesNotExist:
            pass

        try:
            User.objects.get(username=data['username'])
            errors.append('choose another login')
        except User.DoesNotExist:
            pass

        login = data["username"]
        if not login:
            errors.append('enter login')
        elif len(login) < 4:
            errors.append("username >= 4 symbols")

        password = data['password']
        if not password:
            errors.append("enter password")
        elif len(password) < 8:
            errors.append("password >= 8 symbols")

        email = data['email']
        if not email:
            errors.append("enter email")

        if not errors:
            """
            new_form = form.save(commit=False)
            new_form.login = data.get('username')
            new_form.password = data.get('password')
            new_form.email = data.get('email')
            new_form.save()
            form.save_m2m()
            """
            new_user = User(username=data['username'], email=data['email'])
            new_user.set_password(data['password'])
            new_user.save()
            return HttpResponseRedirect("/login/")
    return render(request, 'regPage.html', {"errors": errors, 'names_dict': names_dict, "form": form})



def auth(request):
    names_dict = {}
    errors = []
    form = AuthForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        names_list = ["username", "password"]
        names_dict = {x: request.POST.get(x, "") for x in names_list}
        login = data["username"]
        if not login:
            errors.append('enter login')
        password = data['password']
        if not password:
            errors.append("enter password")

        if not errors:
            try:
                userdata = User.objects.get(username=data["username"])
                if not check_password(data.get('password'), userdata.password):
                    errors.append("invalid password or user does not exist")

            except User.DoesNotExist:
                errors.append("invalid password or user does not exist")

            if not errors:
                user = authenticate(username=login, password=data.get('password'))
                if user is not None:
                    if request.user.is_authenticated:
                        pass
                    login_user(request, user)
                    return HttpResponseRedirect("/about/")
    print(list(errors))
    return render(request, 'loginPage.html', {"errors": errors, 'names_dict': names_dict, "form": form})

"""


def auth(request):
    form = AuthForm(request.POST)
    errors = []
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        login_user(request, user)
        if user is not None:
            if user.is_active:
                login_user(request, user)
                return HttpResponseRedirect("/")
        else:
            errors.append('wrong')
    return render(request, 'loginPage.html', {'form': form})
"""

def sign_out(request):
    logout(request)
    return redirect('/about/')


@login_required
def get_user_details(request):
    return render(request, 'userDetailPage.html', {})


@login_required
def get_user_actions(request):
    actions = Package.objects.filter(pk_user=request.user)

    return render(request, 'userActionsPage.html', {'actions': actions})



def test(request):
    context = Package.objects.get(id=10)
    actions = Package.objects.filter(pk_user=request.user)
    return render(request, 'testPage.html', {'flag': context})