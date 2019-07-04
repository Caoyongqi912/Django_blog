from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Index.urls', namespace='Index')),
    path('spider/', include('spider.urls', namespace='spider')),
    path('user/', include('User.urls', namespace='User')),
    path('articles/',include('Articles.urls',namespace='articles'))
]
