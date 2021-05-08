from django.shortcuts import render
from django.contrib.auth import login, authenticate
from rest_framework import generics, permissions, request
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.parsers import JSONParser
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from .serializers import UserSerializer, RegisterSerializer
# from .models import Post


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

# class LoginAPI(generics.GenericAPIView):
#     if request.method == 'POST':
#         data = JSONParser.parse(request)
#         user = authenticate(request, username=data['username'], password=data['password'])
#         if user is None:
#             return JsonResponse({'error':'Could not login'}, status=400)
#         else:
#             token = Token.objects.get(user=user)
#         return JsonResponse({'token':str(token)},status=201)

# Login
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


# class PostList(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer