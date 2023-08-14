from django.db import models

class ServiceRequest(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    )

    customer_name = models.CharField(max_length=100)
    request_type = models.CharField(max_length=100)
    details = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    submission_time = models.DateTimeField(auto_now_add=True)
    resolution_time = models.DateTimeField(null=True, blank=True)
    attached_files = models.FileField(upload_to='service_request_files/', blank=True, null=True)

    def __str__(self):
        return f"{self.customer_name} - {self.request_type}"

