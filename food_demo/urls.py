"""food_demo URL Configuration

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
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

from food_demo import views as views

urlpatterns = [
    # Django backend
    path('admin/', admin.site.urls),

    # REST API
    path('docs/', include_docs_urls(title="Food Demo", )),

    # variable model url
    path('invitation/', include(('invitation.urls', 'invitation'), namespace='invitation')),
    path('food/', include(('food.urls', 'food'), namespace='food')),
    path('user/', include(('user.urls', 'user'), namespace='user')),

    # / direct view
    path('', views.index),
    path('addbagitem', views.addbagitem),
    path('addmessage', views.addmessage),
    path('bag', views.bag),
    path('invitation', views.invitation),
    path('reci', views.reci),
    path('recipe', views.recipe),
    path('search', views.search),
    path('second', views.second),
    path('person', views.person),
    path('searchresult', views.searchresult),

    path('signin', views.sign_in),
    path('signup', views.sign_up),

    path('test', views.test),
]
