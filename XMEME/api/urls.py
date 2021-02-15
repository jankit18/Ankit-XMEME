from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.FeedList, name = 'feedList'),              # URL to POST and GET Memes
    path('<int:pk>', views.FeedDetail, name = 'feedDetail'),  # URL to PATCH and GET Memes based on meme ID
]

