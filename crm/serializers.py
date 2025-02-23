from rest_framework import serializers
from .models import Customer,Lead,Task,Report,CRMEvent

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
       


class CRMEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CRMEvent
        fields = '__all__'


