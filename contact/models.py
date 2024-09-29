from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    subject=models.CharField(max_length=200)
    message=models.TextField()
    created=models.DateField(auto_now_add=True)
    
    def __str__(self) :
        return f"{self.name} - {self.created}"
