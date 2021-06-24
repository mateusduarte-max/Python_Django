from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Cria a classe da tabela (inserir no banco)
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


# Cria o nome da tabela
    class Meta:
        db_table = 'evento'

    # Altera o nome do evento

    def __str__(self):
        return self.titulo


