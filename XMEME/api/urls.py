from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.ApiOverview, name = 'apiView'),
    path('memes/', views.FeedList, name = 'feedList'),
    path('memes/<int:pk>', views.FeedDetail, name = 'feedDetail'),
]

