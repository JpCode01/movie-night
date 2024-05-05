from pegar_titulos_filmes import PegarTitulosFilmes
from sortear import Sortear
import os

# Instanciando objetos
lista_filmes = PegarTitulosFilmes()
filme_gerado = Sortear(250)

def mensagem_de_erro(mensagem):
        """
        Exibe uma mensagem de erro e inicia a execução novamente
        
        Output: "Opção inválida! Tente novamente."
        """
        os.system('cls')
        print(mensagem)
        main()

def mensagem_final(mensagem):
    """
    Exibe a mensagem final e termina a execução
    
    Output: "Espero que o filme seja bom. 😉"
    Output: "𝕆𝕓𝕣𝕚𝕘𝕒𝕕𝕠 𝕡𝕠𝕣 𝕡𝕒𝕣𝕥𝕚𝕔𝕚𝕡𝕒𝕣 🍿"
    """
    os.system('cls')
    print('Espero que o filme seja bom. 😉')
    print(mensagem)

def exibir_titulo():
    """
    Exibe o título do programa

    Output: O Título
    """
    titulo = '''
    ███╗░░░███╗░█████╗░██╗░░░██╗██╗███████╗  ███╗░░██╗██╗░██████╗░██╗░░██╗████████╗
    ████╗░████║██╔══██╗██║░░░██║██║██╔════╝  ████╗░██║██║██╔════╝░██║░░██║╚══██╔══╝
    ██╔████╔██║██║░░██║╚██╗░██╔╝██║█████╗░░  ██╔██╗██║██║██║░░██╗░███████║░░░██║░░░
    ██║╚██╔╝██║██║░░██║░╚████╔╝░██║██╔══╝░░  ██║╚████║██║██║░░╚██╗██╔══██║░░░██║░░░
    ██║░╚═╝░██║╚█████╔╝░░╚██╔╝░░██║███████╗  ██║░╚███║██║╚██████╔╝██║░░██║░░░██║░░░
    ╚═╝░░░░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝╚══════╝  ╚═╝░░╚══╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░          
    '''
    print(titulo)
    tamanho = len(titulo)
    tamanho_dividido_por_6 = tamanho // 6
    print('━' * tamanho_dividido_por_6)

def exibir_resultado():
    """
    Exibe o resultado do sorteio

    Input: tipo de sorteio (imdb ou lista), deixa lower case como padrão 

    Output: "𝕆𝕓𝕣𝕚𝕘𝕒𝕕𝕠 𝕡𝕠𝕣 𝕡𝕒𝕣𝕥𝕚𝕔𝕚𝕡𝕒𝕣 🍿" (opção: lista)
    """
    tipo_de_sorteio = input('\nSeja bem vindo ao Movie Night! O sorteio será do imdb ou definido pelo usuário? (imdb/lista) ')
    tipo_de_sorteio.lower()
    if tipo_de_sorteio == 'imdb':
        input('\nDigite uma tecla qualquer e aguarde: ')
        # Chamar os métodos 
        lista_filmes.top250_imdb
        filme_gerado.filme_imdb_sorteado
        # chama função para repetir 
        repetir_novamente()
    elif tipo_de_sorteio == 'lista':
        # Chama o método
        filme_gerado.filme_usuario_sorteado
        exibir_bom_filme()
        input('\nDigite uma tecla qualquer: ')
        # Finaliza o programa, na opção lista não será repetido
        os.system('cls')
        print('𝕆𝕓𝕣𝕚𝕘𝕒𝕕𝕠 𝕡𝕠𝕣 𝕡𝕒𝕣𝕥𝕚𝕔𝕚𝕡𝕒𝕣 🍿')
    else:
        mensagem_de_erro('Opção inválida! Tente novamente.')

def exibir_bom_filme():
    """
    Exibe a mensagem Bom Filme!

    Output: "Bom Filme!"
    """
    print('''
    ██████╗░░█████╗░███╗░░░███╗  ███████╗██╗██╗░░░░░███╗░░░███╗███████╗██╗
    ██╔══██╗██╔══██╗████╗░████║  ██╔════╝██║██║░░░░░████╗░████║██╔════╝██║
    ██████╦╝██║░░██║██╔████╔██║  █████╗░░██║██║░░░░░██╔████╔██║█████╗░░██║
    ██╔══██╗██║░░██║██║╚██╔╝██║  ██╔══╝░░██║██║░░░░░██║╚██╔╝██║██╔══╝░░╚═╝
    ██████╦╝╚█████╔╝██║░╚═╝░██║  ██║░░░░░██║███████╗██║░╚═╝░██║███████╗██╗
    ╚═════╝░░╚════╝░╚═╝░░░░░╚═╝  ╚═╝░░░░░╚═╝╚══════╝╚═╝░░░░░╚═╝╚══════╝╚═╝
    ''')

def repetir_novamente():
    """
    Repete a execução caso o usuário queira(apenas com a opção imdb)

    Input: "Deseja trocar de filme? s/n ", deixa lower case como padrão 
    """
    input_repeticao = input('Deseja trocar de filme? s/n ')
    input_repeticao.lower()
    
    if input_repeticao == 's':
        # Limpa o consele e executa o programa novamente
        os.system('cls')
        main()
    elif input_repeticao == 'n':
        mensagem_final('𝕆𝕓𝕣𝕚𝕘𝕒𝕕𝕠 𝕡𝕠𝕣 𝕡𝕒𝕣𝕥𝕚𝕔𝕚𝕡𝕒𝕣 🍿')
    else:
        print('Opção inválida! Tente novamente.')
        repetir_novamente()

def main():
    """Execução de todo o programa"""
    exibir_titulo()
    exibir_resultado()

if __name__ == '__main__':
    main()