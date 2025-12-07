from django.db import models

# Create your models here.


class EnquiryRequest(models.Model):
    """
    Stores a single enquiry request message
    """

    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Enquiry request from {self.name}"
