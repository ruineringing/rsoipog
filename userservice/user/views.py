from user.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from user.serializers import UserSerializer
 
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
 
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
 
    def get_queryset(self):
        return User.objects.all().filter(id=self.kwargs['pk'])