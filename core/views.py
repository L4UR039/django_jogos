from django.shortcuts import render, get_object_or_404, redirect
from .models import Desenvolvedor, Jogo

def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')

def listar_desenvolvedores(request):
    desenvolvedores = Desenvolvedor.objects.all()
    return render(request, 'desenvolvedor/listar.html', {'desenvolvedores': desenvolvedores})

def criar_desenvolvedor(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        pais = request.POST['pais']
        fundacao = request.POST['fundacao']
        Desenvolvedor.objects.create(nome=nome, pais=pais, fundacao=fundacao)
        return redirect('listar_desenvolvedores')
    return render(request, 'desenvolvedor/criar.html')

def editar_desenvolvedor(request, id):
    desenvolvedor = get_object_or_404(Desenvolvedor, id=id)
    if request.method == 'POST':
        desenvolvedor.nome = request.POST['nome']
        desenvolvedor.pais = request.POST['pais']
        desenvolvedor.fundacao = request.POST['fundacao']
        desenvolvedor.save()
        return redirect('listar_desenvolvedores')
    return render(request, 'desenvolvedor/editar.html', {'desenvolvedor': desenvolvedor})

def deletar_desenvolvedor(request, id):
    desenvolvedor = get_object_or_404(Desenvolvedor, id=id)
    desenvolvedor.delete()
    return redirect('listar_desenvolvedores')


def listar_jogos(request):
    jogos = Jogo.objects.all()
    return render(request, 'jogo/listar.html', {'jogos': jogos})

def criar_jogo(request):
    desenvolvedores = Desenvolvedor.objects.all()
    if request.method == 'POST':
        nome = request.POST['nome']
        genero = request.POST['genero']
        ano_lancamento = request.POST['ano_lancamento']
        desenvolvedor_id = request.POST['desenvolvedor']
        desenvolvedor = get_object_or_404(Desenvolvedor, id=desenvolvedor_id)
        Jogo.objects.create(nome=nome, genero=genero, ano_lancamento=ano_lancamento, desenvolvedor=desenvolvedor)
        return redirect('listar_jogos')
    return render(request, 'jogo/criar.html', {'desenvolvedores': desenvolvedores})

def editar_jogo(request, id):
    jogo = get_object_or_404(Jogo, id=id)
    desenvolvedores = Desenvolvedor.objects.all()
    if request.method == 'POST':
        jogo.nome = request.POST['nome']
        jogo.genero = request.POST['genero']
        jogo.ano_lancamento = request.POST['ano_lancamento']
        desenvolvedor_id = request.POST['desenvolvedor']
        jogo.desenvolvedor = get_object_or_404(Desenvolvedor, id=desenvolvedor_id)
        jogo.save()
        return redirect('listar_jogos')
    return render(request, 'jogo/editar.html', {'jogo': jogo, 'desenvolvedores': desenvolvedores})

def deletar_jogo(request, id):
    jogo = get_object_or_404(Jogo, id=id)
    jogo.delete()
    return redirect('listar_jogos')
