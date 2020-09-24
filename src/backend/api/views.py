from django.forms import model_to_dict
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def login(request):
    if request.method == 'GET':
        raise MethodNotAllowed('GET')

    if request.method == 'POST':
        serializer = AuthTokenSerializer(
            data=request.data,
            context={
                'request': request,
            },
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': model_to_dict(user)
        })
