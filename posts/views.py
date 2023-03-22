from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(["GET","POST"])
def homepage(request:Request):
    if(request.method=="POST"):
        data=request.data
        response={"message":"hello","data":data}
        return Response(response,status=status.HTTP_201_CREATED)
    response={"message":"hello"}
    return Response(response,status=status.HTTP_200_OK)

    





