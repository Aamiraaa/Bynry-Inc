from django.shortcuts import render, get_object_or_404, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm

def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save()
            return redirect('track_service_request', request_id=service_request.id)
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_service_request.html', {'form': form})

def track_service_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    return render(request, 'track_service_request.html', {'service_request': service_request})


