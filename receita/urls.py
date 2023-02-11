from django.urls import path
from receita.views import home, pudim, sorvete


urlpatterns = [
    path('home', home),
    path('pudim/', pudim),
    path('sorvete', sorvete)
]
