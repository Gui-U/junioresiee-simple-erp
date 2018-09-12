from django.shortcuts import render

# Create your views here.
from myapp.models import Student, Mandate

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_mandate = Mandate.objects.count()
    
    context = {
        'num_mandate': num_mandate,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from myapp.models import DocTechnicalReport

def docTechnicalReport_details(request, pk):
    doc_tech = get_object_or_404(DocTechnicalReport, pk=pk)
    return render(request, 'myapp/doctechnicalreport_detail.html', context={'doc_tech': doc_tech})

class DocTechnicalReportListView(ListView):
    model = DocTechnicalReport

class docTechnicalReportCreate(CreateView):
    model = DocTechnicalReport
    fields = '__all__'

class docTechnicalReportUpdate(UpdateView):
    model = DocTechnicalReport
    fields = '__all__'

class docTechnicalReportDelete(DeleteView):
    model = DocTechnicalReport
    success_url = reverse_lazy('doctech-list')

def docTechnicalReport_topdf(request, pk):
    """A view that streams a LaTeX generated pdf."""
    typedoc="technical_report"
    doc_tech = get_object_or_404(DocTechnicalReport, pk=pk)
    return doc_tech.download_latex_doc(typedoc)

    


