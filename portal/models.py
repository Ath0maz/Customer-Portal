from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Outros campos...

class Ticket(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=[('aberto', 'Aberto'), ('fechado', 'Fechado')])
    # Outros campos...
