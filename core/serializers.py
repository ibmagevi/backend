from allauth.account.adapter import get_adapter
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from . import models
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ('email', 'username', 'password', 'is_student', 'is_owner', 'is_admin', 'is_employee', 'notification_token')

class CustomRegisterSerializer(RegisterSerializer):
    is_agent = serializers.BooleanField()
    is_user = serializers.BooleanField()

    class Meta:
        model = models.User
        fields = ('email', 'username', 'password', 'is_student', 'is_owner', 'is_admin', 'is_employee', 'notification_token')

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'is_agent': self.validated_data.get('is_agent', ''),
            'is_user': self.validated_data.get('is_user', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.is_agent = self.cleaned_data.get('is_agent')
        user.is_user = self.cleaned_data.get('is_user')
        user.save()
        adapter.save_user(request, user, self)
        return user

class TokenSerializer(serializers.ModelSerializer):
    user_type = serializers.SerializerMethodField()

    class Meta:
        model = Token
        fields = ('key', 'user', 'user_type')

    def get_user_type(self, obj):
        serializer_data = UserSerializer(
            obj.user
        ).data
        is_agent = serializer_data.get('is_agent')
        is_user = serializer_data.get('is_user')
        return {
            'is_agent': is_agent,
            'is_user': is_user,
        }

class HospitalSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Hospital
        fields = "__all__"

class AgentProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AgentProfile
        fields = "__all__"

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AgentProfile
        fields = "__all__"

class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Report
        fields = "__all__"

class HospitalCommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.HospitalComments
        fields = "__all__"

class TestingSlotBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TestingSlotBooking
        fields = "__all__"

class QuarantineBedSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TestingSlotBooking
        fields = "__all__"

class QuarantineBedBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.QuarantineBedBooking
        fields = "__all__"

