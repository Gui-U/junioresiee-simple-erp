from rest_framework import routers
from restapi import views

router = routers.SimpleRouter()
router.register(r'student', views.StudentViewSet)
router.register(r'mandate', views.MandateViewSet)
router.register(r'doctech', views.DocTechnicalReportViewSet)


from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

# Create our schema's view w/ the get_schema_view() helper method. Pass in the proper Renderers for swagger
schema_view = get_schema_view(title='REST API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

from django.urls import path
from django.conf.urls import include
# Inlcude the schema view in our urls.
urlpatterns = [
    path('', schema_view, name="api-doc"),
    path('', include(router.urls), name="api-doc-detail"),
]
