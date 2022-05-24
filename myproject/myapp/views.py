from django.shortcuts import render
from .models import Message as msg
from .serializers import MessageSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes,authentication_classes
# Create your views here.
class CustomAuthTokenLogin(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
#@authentication_classes([TokenAuthentication])
#@permission_classes([IsAuthenticated])
class Message(viewsets.ModelViewSet):
    queryset = msg.objects.all().values()

    serializer_class = MessageSerializer
    def get_queryset(self):#(self, request, *args, **kwargs):
        asd = msg.objects.filter(username=self.request.user.pk).all()
       # print(asd)
      #  for a in asd:
       #     id = a.id
        #    aw= a.created_by()
         #   print(aw)
        return asd

        return Response({
            "id":'a',

            "message": "Lorem ipsum",

            "created_at": "created time in UTC",

            "updated_at": "last updated time in UTC",

                          "c":aw
        })
