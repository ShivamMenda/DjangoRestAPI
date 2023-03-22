from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer
@api_view(["GET","POST"])
def homepage(request:Request):
    if(request.method=="POST"):
        data=request.data
        response={"message":"hello","data":data}
        return Response(response,status=status.HTTP_201_CREATED)
    response={"message":"hello"}
    return Response(response,status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def listPosts(request:Request):
    posts=Post.objects.all()
    serializer=PostSerializer(instance=posts,many=True)
    response={
        "message":"Posts Retrieved",
        "data":serializer.data
    }
    return Response(data=response,status=status.HTTP_200_OK)

@api_view(http_method_names=["POST"])
def create_post(request:Request):
    data=request.data
    s=PostSerializer(data=data)
    if s.is_valid():
        s.save()
        resp={
            "message":"Post Created",
            "data":s.data
        }
        return Response(data=resp,status=status.HTTP_201_CREATED)
    return Response(data=s.errors,status=status.HTTP_400_BAD_REQUEST)





