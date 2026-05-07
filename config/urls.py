from django.contrib import admin
from django.urls import path, include
from home import urls as home_urls
from posts import urls as posts_urls
from accounts import urls as accounts_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    #path('' , include(home_urls , namespace='home')),
    path('api/auth', include(accounts_urls , namespace='accounts')),
    path('api/posts', include(posts_urls , namespace='posts')),
]
