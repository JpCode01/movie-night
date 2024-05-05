from pegar_titulos_filmes import PegarTitulosFilmes
# Importa uma biblioteca para gerar um número pseudoaleatório
from random import randint
# Importa a Biblioteca IMDbPY(cinemagoer)
from imdb import IMDb

app = IMDb()

class Sortear(PegarTitulosFilmes):
    """
    Classe filho que sorteia um filme baseado no índice do array(imdb ou do usuário)
    
    """
    def __init__(self, quantidade_filmes):
        super().__init__()
        self._quantidade_filmes = quantidade_filmes

    @property
    def filme_imdb_sorteado(self):   
            """
            Método para atribuir na variável "sorteado" o elemento gerado (índice)
            
            Output: O filme da noite
            """
            super().top250_imdb
            sorteado = self._titulo[randint(0,self._quantidade_filmes - 1)]
            results = app.search_movie(sorteado)
            if results:
                # Obter o filme mais relevante da lista de resultados
                movie = results[0]
                
                # Carregar informações adicionais sobre o filme
                app.update(movie)
                
                # Obter o ano de lançamento do filme
                release_year = movie['year']
                # Exibição do filme sorteado
                exibicao = f'\nSeu filme da noite é: {sorteado} ({release_year})'
                print(exibicao)
                print('━' * len(exibicao))
    
    @property
    def filme_usuario_sorteado(self):
        """
        Método para atribuir na variável "Sorteado" o elemento gerado (índice)
        
        """
        super().filmes_usuario
        tamanho_array = len(self._titulo)
        # Gera um índice 
        sorteado = self._titulo[randint(0,tamanho_array - 1)]
        exibicao = f'\nSeu filme da noite é: {sorteado}'
        print(exibicao)
        print('━' * len(exibicao))
    
