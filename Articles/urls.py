from django.urls import path

from Articles.views import Detail, Add_Comment

app_name = "articles"
urlpatterns = [
    path('detail/<int:aid>',Detail.as_view(),name='detail'),
    path('add_comment/<int:aid>',Add_Comment.as_view(),name='add_comment')
]