

# Create your models here.
from django.db import models

class Certificate(models.Model):
    title = models.CharField(max_length=100)
    recipient_name = models.CharField(max_length=100)
    completion_date = models.DateField()
    certificate_file = models.FileField(upload_to='certificates/')

    # Additional fields for verification integrity (e.g., hash or signature)
    # ...

    def __str__(self):
        return self.title
