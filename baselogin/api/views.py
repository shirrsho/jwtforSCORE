from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth import get_user_model

from .forms import NewUserForm


User = get_user_model()

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        print(user.username)
        token['username'] = user.username
        token['email'] = user.email

        # ...

        return token
    
    # def validate(self, attrs):
    #     credentials = {
    #         'username': '',
    #         'password': attrs.get("password")
    #     }
    #     print(attrs)
        
    #     user_obj = User.objects.filter(email=attrs.get("username")).first()
    #     if user_obj:
    #         credentials['username'] = user_obj.username
        
    #     return super().validate(credentials)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def register_request(request):
    form = NewUserForm(data=request.data)
    # emails = User.objects.filter(email=request.data.email)
    # usernames = User.objects.filter(username=request.data.username)
    print(request.data)
    if form.is_valid():
        form.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)