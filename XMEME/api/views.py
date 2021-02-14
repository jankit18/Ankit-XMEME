
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserContentSerializer
from meme.models import ContentImage


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'memes' : '/memes',
        'userMeme' : '/memes/<int:pk>'
    }
    return Response(api_urls)

@api_view(['GET','POST'])
def FeedList(request):
    serializer=""
    if request.method == 'POST':
        serializer = UserContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
    else:
        allContent = ContentImage.objects.all().order_by('-id')[:100]
        serializer = UserContentSerializer(allContent, many=True)

    return Response(serializer.data)


@api_view(['GET','PATCH'])
def FeedDetail(request,pk):    
    print("yoo")
    allContent = ContentImage.objects.get(id=pk)
    serializer=""
    if request.method == 'GET':
        serializer = UserContentSerializer(allContent, many=False)
    else:
        print(request.data)
        serializer = UserContentSerializer(instance=allContent, data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()

    return Response(serializer.data)