from django.contrib import admin

# Register your models here.

from myapp.models import Student, Mandate, DocTechnicalReport

admin.site.register(Student)
admin.site.register(Mandate)
admin.site.register(DocTechnicalReport)
