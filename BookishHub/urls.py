"""
URL configuration for bookish project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from discussion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('create_room/', views.create_room_view, name='create_room'),
    path('post_message/<int:room_id>/', views.post_message_view, name='post_message'),
    path('discussion_room/<int:room_id>', views.discussion_room, name="discussion_room"),
    path('search_rooms/', views.search_rooms, name='search_rooms'),
    path('delete_room/<int:room_id>', views.delete_room, name='delete_room'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)