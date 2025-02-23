from django.db import models
from django.contrib.auth.models import User
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Lead(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('new', 'New'), ('in_progress', 'In Progress'), ('won', 'Won'), ('lost', 'Lost')])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.customer.name} - {self.status}"
class Task(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.TextField()
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    lead = models.ForeignKey(Lead, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_closed = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending')

    def __str__(self):
        return f"Sale: {self.customer.name} - {self.amount}"
class Contact(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.contact_person} ({self.customer.name})"
class Report(models.Model):
    REPORT_TYPES = [
        ('sales', 'Sales Report'),
        ('task', 'Task Report'),
        ('lead', 'Lead Report'),
        ('customer', 'Customer Report'),
    ]

    title = models.CharField(max_length=255)
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title

class CRMEvent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    client_name = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=50, default='Scheduled')

    def __str__(self):
        return self.title
class CRMEmail(models.Model):
    subject = models.CharField(max_length=255)
    recipient = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')  # Sent, Failed, etc.

    def __str__(self):
        return f"{self.subject} to {self.recipient}"

class Event(models.Model):
    title = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    reminder = models.BooleanField(default=False)  # ✅ Reminder Flag
    reminder_time = models.DateTimeField(null=True, blank=True)  # ⏰ When to trigger

    def __str__(self):
        return self.title