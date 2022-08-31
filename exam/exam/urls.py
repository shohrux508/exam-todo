"""exam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app1.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('plans/', plan),
    path('student/', students),
    path('', hello),
    path('delete-student/<int:a>/', delete_student),
    path('delete-plan/<int:id>/', delete_plan),
    path('add-student/', add_student),
    path('add-plan/', add_plan),
    path('add-plans/', plan_add_data),
    path('student-up/<int:a>/', student_up_data),
    path('plan-up/<int:id>/', plan_up_data),
    path('plan-save/<int:id>/', plan_update),
    path('student-save/<int:id>/', student_update),



]
