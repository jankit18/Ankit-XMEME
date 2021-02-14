from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.FeedList, name = 'feedList'),
    path('<int:pk>', views.FeedDetail, name = 'feedDetail'),
]

