from django.shortcuts import render
from . import models, serializers
from rest_framework import viewsets, status, permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_list_or_404, get_object_or_404
import datetime
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.db.models import Q


# Create your views here.
class HospitalAPIViewSet(viewsets.ModelViewSet):
    queryset = models.Hospital.objects.all()
    serializer_class = serializers.HospitalSerializer
    permission_classes = [permissions.IsAuthenticated, ]

class AgentProfileAPIViewSet(viewsets.ModelViewSet):
    queryset = models.AgentProfile.objects.all()
    serializer_class = serializers.AgentProfileSerializer
    permission_classes = [permissions.IsAuthenticated, ]

class UserProfileAPIViewSet(viewsets.ModelViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated, ]

class ReportAPIViewSet(viewsets.ModelViewSet):
    queryset = models.Report.objects.all()
    serializer_class = serializers.ReportSerializer
    permission_classes = [permissions.IsAuthenticated, ]

class HospitalCommentsAPIViewSet(viewsets.ModelViewSet):
    queryset = models.HospitalComments.objects.all()
    serializer_class = serializers.HospitalCommentsSerializer
    permission_classes = [permissions.IsAuthenticated, ]

class TestingSlotBookingAPIViewSet(viewsets.ModelViewSet):
    queryset = models.TestingSlotBooking.objects.all()
    serializer_class = serializers.TestingSlotBookingSerializer
    permission_classes = [permissions.IsAuthenticated, ]

class QuarantineBedAPIViewSet(viewsets.ModelViewSet):
    queryset = models.QuarantineBed.objects.all()
    serializer_class = serializers.QuarantineBedSerializer
    permission_classes = [permissions.IsAuthenticated, ]

class QuarantineBedBookingAPIViewSet(viewsets.ModelViewSet):
    queryset = models.QuarantineBedBooking.objects.all()
    serializer_class = serializers.QuarantineBedBookingSerializer
    permission_classes = [permissions.IsAuthenticated, ]

