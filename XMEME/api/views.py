
from rest_framework.decorators import api_view  # Importing api_view from rest_framework decorators
from rest_framework.response import Response    # Importing Response from rest_framework.response

from .serializers import UserContentSerializer  # Importing ContentImage from meme app model
from meme.models import ContentImage      # Importing ContentImage from meme app model



# GET for Fetching Recent 100 MEMES Sorted Based On Ascending Submission Time
# POST for Posting New Meme

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


# GET for Fetching the meme with (id=pk)
# PATCH for Updating the meme with (id=pk)

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