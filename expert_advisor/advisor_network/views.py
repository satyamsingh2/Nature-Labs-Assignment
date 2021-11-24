from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import CreateAdvisorSerializer, \
    RegisterUserSerializer, LoginUserSerializer, \
    AdvisorListSerializer, BookAdvisorSerializer, BookingSerializer
from .models import Advisor, User, Booking
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.tokens import RefreshToken

class CreateAdvisorView(CreateAPIView):
    queryset = Advisor.objects.all()
    serializer_class = CreateAdvisorSerializer

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class RegisterUserView(CreateAPIView):
    serializer_class = RegisterUserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LoginUserView(GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request):
        try:
            data =request.data
            if not data['email'] or not data['password']:
                response_data = {
                    'error': 'email or password cannot be empty'
                }

                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.get(email=data['email'], password=data['password'])
            refresh_token = RefreshToken.for_user(user)
            response_data ={
                'id': user.id,
                'access_token': str(refresh_token.access_token),
                'refresh_token': str(refresh_token)
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            response_data = {
                'error': 'please enter correct password'
            }
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)

class AdvisorListView(ListAPIView):
    serializer_class = AdvisorListSerializer
    queryset = Advisor.objects.all()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class BookAdvisorView(CreateAPIView):
    serializer_class = BookAdvisorSerializer

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
        except:
            return Response({'error': 'please enter correct user id or advisor id'}, status=status.HTTP_400_BAD_REQUEST)


class BookingView(ListAPIView):
    serializer_class = BookingSerializer
    lookup_url_kwarg = "user_id"

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return Booking.objects.filter(user_id=user_id)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

