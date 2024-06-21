"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.template.context_processors import static
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from postings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello_page),
    path('posts/' , views.post_list_page),
    path('posting/', views.posting_page, ),
    path('option/', views.opt_page),
    path("account/register/", views.register_page),
    path("account/login/", views.login_page),
    path("accounts/login/", views.login_page),
    path("account/logout/", views.logout_page),
    path('post_comment/', views.new_comment),
    path('posts/<int:id>', views.post_page),
    path('profile/', views.profile_page)
]