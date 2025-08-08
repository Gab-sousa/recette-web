from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Receita, Ingrediente, Avaliacao, ReceitaIA
from .forms import ReceitaForm, IngredienteForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models import Avg
from django.contrib import messages
import os
from groq import Groq 
from .forms import GerarReceitaIAForm
from dotenv import load_dotenv
load_dotenv()
import re




@login_required
def criar_ingrediente(request):
    form = IngredienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_ingredientes')
    return render(request, 'ingredientes/criar.html', {'form': form})

@login_required
def lista_ingredientes(request):
    query = request.GET.get('q')
    ingredientes = Ingrediente.objects.all().order_by('nome') 
    if query:
        ingredientes = ingredientes.filter(nome__icontains=query)
    return render(request, 'ingredientes/lista.html', {'ingredientes': ingredientes})

@login_required
def criar_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            receita = form.save(commit=False)
            receita.autor = request.user
            receita.save()
            form.save_m2m()
            return redirect('lista_receitas')
    else:
        form = ReceitaForm()
    return render(request, 'receitas/criar.html', {'form': form})

@login_required
def lista_receitas(request):
    receitas = Receita.objects.all()
    return render(request, 'receitas/lista.html', {'receitas': receitas})


@login_required
def adicionar_favorito(request, receita_id):
    receita = get_object_or_404(Receita, id=receita_id)
    receita.favoritos.add(request.user)
    return redirect('lista_receitas')

@login_required
def remover_favorito(request, receita_id):
    receita = get_object_or_404(Receita, id=receita_id)
    receita.favoritos.remove(request.user)
    return redirect('lista_receitas')

@login_required
def minhas_favoritas(request):
    favoritas = request.user.receitas_favoritas.all()
    return render(request, 'receitas/favoritas.html', {'receitas': favoritas})

def lista_receitas(request):
    query = request.GET.get('q')
    receitas = Receita.objects.all()

    if query:
        receitas = receitas.filter(
            Q(titulo__icontains=query) |
            Q(ingredientes__nome__icontains=query)
        ).distinct()

    return render(request, 'receitas/lista.html', {'receitas': receitas})


def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')


@login_required
def detalhe_receita(request, receita_id):
    receita = get_object_or_404(Receita, id=receita_id)
    media_avaliacoes = receita.avaliacoes.aggregate(Avg('nota'))['nota__avg'] or 0
    return render(request, 'receitas/detalhe.html', {
        'receita': receita,
        'media_avaliacoes': media_avaliacoes
    })

@login_required
def avaliar_receita(request, receita_id):
    receita = get_object_or_404(Receita, id=receita_id)
    nota = int(request.POST.get('nota'))

    avaliacao, created = Avaliacao.objects.update_or_create(
        receita=receita,
        usuario=request.user,
        defaults={'nota': nota}
    )

    messages.success(request, "Avaliação salva com sucesso.")
    return redirect('detalhe_receita', receita_id=receita.id)

@login_required
def excluir_receita(request, receita_id):
    receita = get_object_or_404(Receita, id=receita_id)

    if receita.autor != request.user:
        messages.error(request, "Você não tem permissão para excluir esta receita.")
        return redirect('detalhe_receita', receita_id=receita.id)

    receita.delete()
    messages.success(request, "Receita excluída com sucesso.")
    return redirect('lista_receitas')

def gerar_receita_ia(request):
    if request.method == 'POST':
        form = GerarReceitaIAForm(request.POST)
        if form.is_valid():
            ingredientes = form.cleaned_data['ingredientes']
            ingredientes_lista = ', '.join([i.nome for i in ingredientes])

            client = Groq(api_key=os.getenv("GROQ_API_KEY"))

            prompt = f"""
            Crie uma receita detalhada usando apenas estes ingredientes: {ingredientes_lista}.
            Se quiser, use água ou temperos básicos (sal, alho, cebola, azeite).
            A resposta deve conter:
            - Título
            - Ingredientes
            - Equipamentos
            - Instruções
            - Quantas porções serve

            
            """

            resposta = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "Você é um assistente culinário que gera receitas em Markdown."},
                    {"role": "user", "content": prompt}
                ],
                model="llama3-8b-8192",
            ).choices[0].message.content

            
            linhas = resposta.split('\n')
            titulo = linhas[0].replace('#', '').strip()
            descricao = resposta  

            nova_receita = ReceitaIA.objects.create(
                titulo=titulo,
                descricao=descricao, 
            )
            nova_receita.ingredientes.set(ingredientes)
            nova_receita.save()

            return redirect('lista_receitas')
    else:
        form = GerarReceitaIAForm()
    
    return render(request, 'receitas/gerar_ia.html', {'form': form})

@login_required
def lista_receitas_ia(request):
    receitas = ReceitaIA.objects.all()
    return render(request, 'receitas/lista_ia.html', {'receitas': receitas})