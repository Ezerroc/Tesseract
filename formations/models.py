from django.db import models
from django.urls import reverse

class Formation(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pdf_file = models.FileField(upload_to='pdfs/', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_pdf_url(self):
        return reverse('formation_pdf', args=[str(self.id)])