from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('doc_tech', views.DocTechnicalReportListView.as_view(), name='doctech-list'),
    path('doc_tech/create', views.docTechnicalReportCreate.as_view(), name='doctech-create'),
    path('doc_tech/<int:pk>', views.docTechnicalReport_details, name='doctech-detail'),
    path('doc_tech/<int:pk>/update', views.docTechnicalReportUpdate.as_view(), name='doctech-update'),
    path('doc_tech/<int:pk>/delete', views.docTechnicalReportDelete.as_view(), name='doctech-delete'),
    path('doc_tech/<int:pk>/download', views.docTechnicalReport_topdf, name='doctech-pdf'),
]
