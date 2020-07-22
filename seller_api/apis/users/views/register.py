from rest_framework.views import APIView
from seller_api.apis.users.serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


class SellerRegistration(APIView):
    """
    Create seller user
    """
    def post(self, request, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                _token = Token.objects.create(user=user)
                _res_data = serializer.data
                _res_data['token'] = _token.key
                _res_data.pop('password')
                return Response(_res_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)
