from django.db import models

# Create your models here.

#class dos produtos.

class Product(models.Model):
    Produto = models.CharField(max_length = 100)
    valor = models.DecimalField(max_digits= 10, decimal_places = 2)
    quantidade = models.IntegerField()
    produto_id = models.AutoField(primary_key = True)
    descricao = models.TextField()
    
    def __str__(self):
        return self.nome
    
#Clientes.
class Cliente (models.Model):
    nome = models.CharField(max_length= 100)
    senha = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.nome

