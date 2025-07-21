from django.db import models
from django.contrib.auth.models import User

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def _str_(self):
        return self.nome

class Receita(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    ingredientes = models.ManyToManyField(Ingrediente)
    instrucoes = models.TextField()
    equipamentos = models.TextField()
    porcoes = models.PositiveIntegerField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receitas_criadas')
    favoritos = models.ManyToManyField(User, related_name='receitas_favoritas', blank=True)

    def _str_(self):
        return self.titulo

class Avaliacao(models.Model):
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE, related_name='avaliacoes')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nota = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # 1 a 5 estrelas
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('receita', 'usuario')  # Um user só pode avaliar uma vez

    def _str_(self):
        return f"{self.usuario} avaliou {self.receita} com nota {self.nota}"
    
class ReceitaIA(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    ingredientes = models.ManyToManyField(Ingrediente)
    

    def _str_(self):
        return self.titulo