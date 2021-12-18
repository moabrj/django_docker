from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from libraryapp.serializers import UserSerializer
from libraryapp.models import User

class UserView(APIView):
    """
    User api view
    """
    
    #@api_view(['GET', 'POST', 'DELETE'])
    def get(self, request, pk=None):
        # GET list of users, POST a new user, DELETE all users
        if request.method == 'GET':
            users = User.objects.all()
            print(request)
            if pk is not None:
                users = users.filter(pk=pk)
        
            users_serializer = UserSerializer(users, many=True)
            return JsonResponse(users_serializer.data, safe=False)

