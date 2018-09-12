from django.db import models

# Create your models here.


class Student(models.Model):
    """Model representing a student."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=False)
    date_of_diploma = models.DateField(blank=False)

    class Meta:
        ordering = ['last_name', 'first_name']
    
    def get_absolute_url(self):
        """Returns the url to access a particular student instance."""
        return reverse('student-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'


class Mandate(models.Model):
    """Model representing a mandate."""
    date_of_begin = models.DateField(blank=False)
    
    def get_absolute_url(self):
        """Returns the url to access a particular mandate instance."""
        return reverse('mandate-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.date_of_begin}'

from django.urls import reverse
import os, subprocess, re
from django.http import FileResponse

class DocTechnicalReport(models.Model):
    """Model representing a DocTechnicalReport."""
    tagEtudeNum = models.CharField(max_length=100)
    tagDocNameShort = models.CharField(max_length=100)
    tagDocName = models.CharField(max_length=100)
    tagDocDate = models.CharField(max_length=100)
    tagClientCompagny = models.CharField(max_length=100)
    tagCommercialNom = models.CharField(max_length=100)
    tagCommercialPrenom = models.CharField(max_length=100)
    tagDocVersion = models.CharField(max_length=100)
    


    def download_latex_doc(download_object, typedoc):
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
                #print(allattributes[onekey])
                regex_pattern = re.compile(r"\\newcommand{\\"+ onekey +r"}{[a-zA-Z0-9_. -]+}")
                update_vars(path_filevarslatex, regex_pattern, onekey, allattributes[onekey])

        result_command = subprocess.run(['make', 'DOC='+typedoc],stdout=subprocess.PIPE ,stderr=subprocess.STDOUT )
        #print(result_command.stdout)

        response = FileResponse(open('main.pdf', 'rb'))
        os.chdir(currentdir) # restore current directory path
        response['Content-Disposition'] = 'attachment; filename="' + typedoc + '.pdf"'
        return response

    def get_absolute_url(self):
        """Returns the url to access a particular student instance."""
        return reverse('doctech-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.tagDocNameShort}{self.tagEtudeNum}'





