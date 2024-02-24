from django.db import models

# Create your models here.
class PassRequested(models.Model):
    email = models.EmailField()
    requested_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Pass Requested"
        verbose_name_plural = "Passes Requested"
    
class PassIssued(models.Model):
    email = models.EmailField()
    issued_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Pass Issued"
        verbose_name_plural = "Passes Issued"
