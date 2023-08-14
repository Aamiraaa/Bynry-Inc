from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        exclude = ['submission_time']
        fields = ['customer_name', 'request_type','details','status','submission_time','resolution_time','attached_files']