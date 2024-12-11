from django.db import models

class Desenvolvedor(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.CharField(max_length=50, blank=True)
    fundacao = models.IntegerField()

    def __str__(self):
        return self.nome

class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    ano_lancamento = models.PositiveIntegerField()
    desenvolvedor = models.ForeignKey(Desenvolvedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
