from django.db import models

# Create your models here.
class usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.nome