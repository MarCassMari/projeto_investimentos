from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def pagina_inicial(request):
    return HttpResponse('Página padrão pronta para ser preenchida')

def contato_duvidas(request):
    return HttpResponse('Em caso de dúvidas, envie uma mensagem para o email teste@gmail.com.org')

def minha_historia(request):

    pessoa = {'nome': 'Lucius','idade':20, 'hobby': 'Games'}
    return render(request,'investimentos/minha_historia.html', pessoa)