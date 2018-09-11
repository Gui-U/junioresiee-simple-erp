from rest_framework import serializers
from myapp import models

#include all fields of all models
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'

class MandateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mandate
        fields = '__all__'

class DocTechnicalReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DocTechnicalReport
        fields = '__all__'
