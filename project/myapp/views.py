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


import os, subprocess, re
from django.http import FileResponse

def download_latex_doc(typedoc, download_object):
    currentdir = os.getcwd() #backup current directory path
    os.chdir('../jems-docs')
    path_filevarslatex = typedoc+"/vars.default.tex"

    def update_vars(path_filevarslatex, regex_pattern, newvarname, newvar): #change vars in jems-docs folder
        with open(path_filevarslatex, "r") as fichier:
            contenu=fichier.read()
            filevars=contenu.splitlines()
            for numligne,ligne in enumerate(filevars):
                origin=re.findall(regex_pattern, ligne)
                if len(origin) > 0:
                    remplorigin = "\\newcommand{\\" + newvarname + "}{" + newvar + "}"
                    filevars[numligne]=ligne.replace(origin[0], remplorigin)


        with open(path_filevarslatex, "w") as fichier:
            for ligne in filevars[:-1]:
                fichier.write("%s\n" % ligne)
            fichier.write("%s" % filevars[-1])

    allattributes=download_object.__dict__ # change var starting by "tag" in latex file
    for onekey in allattributes.keys():
        if str(onekey).startswith('tag'):
            print(allattributes[onekey])
            regex_pattern = re.compile(r"\\newcommand{\\"+ onekey +r"}{[a-zA-Z0-9_. -]+}")
            update_vars(path_filevarslatex, regex_pattern, onekey, allattributes[onekey])

    result_command = subprocess.run(['make', 'DOC='+typedoc],stdout=subprocess.PIPE ,stderr=subprocess.STDOUT )
    #print(result_command.stdout)

    response = FileResponse(open('main.pdf', 'rb'))
    os.chdir(currentdir) # restore current directory path
    response['Content-Disposition'] = 'attachment; filename="' + typedoc + '.pdf"'
    return response





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
    return download_latex_doc(typedoc, doc_tech)

    


