from rest_framework.serializers import ModelSerializer
from .models import Advisor, User, Booking
from rest_framework_simplejwt.tokens import RefreshToken

class CreateAdvisorSerializer(ModelSerializer):
    class Meta:
        model = Advisor
        fields = '__all__'


class RegisterUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'name',
            'email',
            'password'
        )

    def create(self, validated_data):
        name = validated_data['name']
        validated_data['username'] = (name.strip()).replace(' ', "_")
        user = super().create(validated_data)
        return user


    def to_representation(self, instance):
        refresh_token = RefreshToken.for_user(instance)

        data = {
            'id': instance.id,
            'access_token': str(refresh_token.access_token),
            'refresh_token': str(refresh_token)
        }
        return data

class LoginUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'password'
        )

class AdvisorListSerializer(ModelSerializer):
    class Meta:
        model = Advisor
        fields = (
            'id',
            'name',
            'image_url'
        )

class BookAdvisorSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = ('booking_time',)

    def create(self, validated_data):
        user_id = self.context['request'].parser_context['kwargs']['user_id']
        advisor_id = self.context['request'].parser_context['kwargs']['advisor_id']
        user = User.objects.get(id=user_id)
        advisor = Advisor.objects.get(id=advisor_id)
        validated_data['user'] = user
        validated_data['advisor'] = advisor
        booking = super().create(validated_data)
        return booking


class BookingSerializer(ModelSerializer):
    advisor = AdvisorListSerializer()
    class Meta:
        model = Booking
        fields = (
            'id',
            'booking_time',
            'advisor',
        )