from django.contrib import admin
from .models import Student, Profile
from .assessments.ned_model import NedAssessment
from .assessments.vak_form import VAKAssessment


admin.site.register(Student)
admin.site.register(Profile)
admin.site.register(NedAssessment)
admin.site.register(VAKAssessment)
