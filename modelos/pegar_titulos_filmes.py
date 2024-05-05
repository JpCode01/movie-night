# Importa a Biblioteca IMDbPY(cinemagoer)
from imdb import IMDb

app = IMDb()
# Pegar a lista com o top 250 do imdb
top = app.get_top250_movies()

class PegarTitulosFilmes:
     """
     Classe pai que retorna uma lista de filmes
     
     Output: self._titulo[] (array com os filmes)
     """
     def __init__(self):
          self._titulo = []

     @property
     def top250_imdb(self):
          """
          Método para pegar apenas os títulos dos filmes
          
          """
          for item in top:
               title = item['title']
               self._titulo.append(title)
     
     @property
     def filmes_usuario(self):
          """
          Método para pegar os filmes do usuário e criar um array

          Input: "Digite a quantidade de filmes: "
          Input: "Digite o nome do filme {i + 1}: "
          """
          tamanho_lista = int(input('Digite a quantidade de filmes: '))
          for i in range(0, tamanho_lista, 1):
               nome_para_lista = input(f'Digite o nome do filme {i + 1}: ')
               self._titulo.append(nome_para_lista)
          
     def __str__(self):
          """
          Representação do objeto em string
          """
          return f'{self._titulo}'

