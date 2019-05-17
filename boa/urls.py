"""boa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from delivery import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('test/', views.test, name='textPage'),
    path('admin/', admin.site.urls),
    path('', views.index, name='homePage'),
    path('about/', views.about, name='aboutPage'),
    path('about/activity/', views.activity, name='ourActivityPage'),
    path('about/news/', views.news, name='newsPage'),
    path('about/vacancy/', views.vacancy, name='vacancyPage'),
    path('about/partner/', views.partner, name='partnerPage'),
    path('service/', views.service, name='servicePage'),
    path('delivery/', views.delivery, name='deliveryPage'),
    path('success/', views.success, name='successPage'),
    path('signup/', views.sign_up, name='signUpPage'),
    path('login/', views.auth, name='loginPage'),
    path('logout/', login_required(views.sign_out), name='logout'),
    path('account/details/', views.get_user_details, name='userDetailPage'),
    path('account/actions/', views.get_user_actions, name='userActionsPage'),
]
