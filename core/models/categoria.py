from django.db import models

class Categoria(models.Models):
    descricao = models.CharField(max_length=100)
    
    def __str__(self):
        return self.descricao