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


