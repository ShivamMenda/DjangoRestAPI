from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,APIView
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404


@api_view(["GET","POST"])
def homepage(request:Request):
    if(request.method=="POST"):
        data=request.data
        response={"message":"hello","data":data}
        return Response(response,status=status.HTTP_201_CREATED)
    response={"message":"hello"}
    return Response(response,status=status.HTTP_200_OK)


class PostListCreateView(APIView):
    serializer_class=PostSerializer
    def get(self,request:Request,*args, **kwargs):
        posts=Post.objects.all()
        s=self.serializer_class(instance=posts,many=True)
        return Response(data=s.data,status=status.HTTP_200_OK)
    def post(self,request:Request,*args, **kwargs):
        data=request.data
        s=self.serializer_class(data=data)
        if(s.is_valid()):
            s.save()
            r={"Message":"Post created","data":s.data}
            return Response(data=r,status=status.HTTP_201_CREATED)
        return Response(data=s.errors,status=status.HTTP_400_BAD_REQUEST)
    
class PostRetreiveUpdateDeleteView(APIView):
    ser_class=PostSerializer
    def get(self,request:Request,post_id:int):
        post=get_object_or_404(Post,pk=post_id)
        s=self.ser_class(instance=post)
        return Response(data=s.data,status=status.HTTP_200_OK)
    
    def put(self,request:Request,post_id:int):
        post=get_object_or_404(Post,pk=post_id)
        update_data=request.data
        s=self.ser_class(instance=post,data=update_data)
        if(s.is_valid()):
            s.save()
            r={"Message":"Post Updated","data":s.data}
            return Response(data=r,status=status.HTTP_200_OK)
        return Response(data=s.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request:Request,post_id:int):
        post=get_object_or_404(Post,pk=post_id)
        post.delete()
        r={"Message":"Post deleted"}
        return Response(data=r,status=status.HTTP_204_NO_CONTENT)


# @api_view(http_method_names=["GET"])
# def post_by_id(request:Request,post_id:int):
#     post=get_object_or_404(Post,pk=post_id)
#     s=PostSerializer(instance=post)
#     return Response(data=s.data,status=status.HTTP_200_OK)

# @api_view(http_method_names=["PUT"])
# def update_post(request:Request,post_id:int):
#     post=get_object_or_404(Post,pk=post_id)
#     update_data=request.data
#     s=PostSerializer(instance=post,data=update_data)
#     if(s.is_valid()):
#         s.save()
#         r={
#             "message":"Post updated",
#             "data":s.data
#         }
#         return Response(data=r,status=status.HTTP_200_OK)
#     return Response(data=s.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(http_method_names=["DELETE"])
# def delete_post(request:Request,post_id:int):
#     post=get_object_or_404(Post,pk=post_id)
#     try:
#         post.delete()
#         r={"message":"Post deleted"}
#         return Response(data=r,status=status.HTTP_204_NO_CONTENT)
#     except:
#         r1={"message":"Post cannot be deleted"}
#         return Response(data=r1,status=status.HTTP_400_BAD_REQUEST)

    




