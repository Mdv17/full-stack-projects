"""
URL configuration for todo_list project.

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
# We are importing include bcoz we need to let our projects know about our apps urls
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # The include function basically says we are gonna include a different urls file whenever a user pulls out whatever route it is
    # Take all these routes and send this routing to this url in this case the urls in the base folder
    path('', include('base.urls')),
]
