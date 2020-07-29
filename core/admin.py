from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Hospital)
admin.site.register(AgentProfile)
admin.site.register(UserProfile)
admin.site.register(Report)
admin.site.register(HospitalComments)
admin.site.register(TestingSlotBooking)
admin.site.register(QuarantineBed)
admin.site.register(QuarantineBedBooking)