from products.models import Product
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer

@api_view(['POST'])
def api_home(request,*args, **kwargs):
      # data=Product.objects.first() #GET
      # ser=ProductSerializer(data)
      # return Response(ser.data)
      ser=ProductSerializer(data=request.data)
      if(ser.is_valid()):
         # ins=ser.save()
         # print(ins)
         return Response(ser.data)
      else:
         return Response(ser.errors,status=400)
      
   
   


