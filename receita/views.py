from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

dict_home = {
    'variavel_home': 'Sou uma variável do dicionário'
}


def home(requisicao):
    # return render(requisicao, 'receita/home.html', context=dict_home)
    return render(requisicao, 'receita/pages/home.html', context=dict_home)


dict_pudim = {'variavel_pudim': 'Eu vim do dict_pudim, lá do Views'}


def pudim(parametro):
    return render(parametro, 'receita/pages/pudim.html', context=dict_pudim)


dict_sorvete = {"variavel_sorvete": "vim do dict_sorvete"}


def sorvete(parametro2):
    return render(parametro2, 'receita/pages/sorvete.html', context=dict_sorvete)
