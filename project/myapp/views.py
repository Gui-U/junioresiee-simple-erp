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
