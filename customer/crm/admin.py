from django.contrib import admin
from .models import Customer, Lead,Sale,Task,Contact,Event


admin.site.register(Customer)
admin.site.register(Lead)
admin.site.register(Task)
admin.site.register(Sale)
admin.site.register(Contact)
admin.site.register(Event)