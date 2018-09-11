from myapp import models
from restapi import serializers
from rest_framework import viewsets


class StudentViewSet(viewsets.ModelViewSet):
    """
    Student api access
    """
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

class MandateViewSet(viewsets.ModelViewSet):
    """
    Mandate api access
    """
    queryset = models.Mandate.objects.all()
    serializer_class = serializers.MandateSerializer

class DocTechnicalReportViewSet(viewsets.ModelViewSet):
    """
    DocTechnicalReport api access
    """
    queryset = models.DocTechnicalReport.objects.all()
    serializer_class = serializers.DocTechnicalReportSerializer
