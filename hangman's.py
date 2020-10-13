from random import randint  # biblioteca ramdom

def arvore():
    class Node:
        def __init__(self, data):
            self.data = data
            self.esquerda = None
            self.direita = None

        def __str__(self):
            return str(self.data)

    class BinaryTree:
        def __init__(self, data):
            node = Node(data)
            self.root = Node(data)

    if __name__ == "__main__":
        tree = BinaryTree(rank1)
        if rank2 < rank1:
            tree.root.esquerda = Node(rank2)
            print('\n 1° -', play1,"Pontos:", tree.root)
            print("2° -",play2,"Pontos:",tree.root.esquerda)
        elif rank2 > rank1:
            tree.root.direita = Node(rank2)
            print("\n1° -", play2, "Pontos:", tree.root.direita)
            print("2° -",play1, "Pontos: ",tree.root)
        else:
            tree.root.direita = Node(rank2)
            print("\n", play1,"e", play2, "terminou empatados com",tree.root, "pontos")


def arvore2():
    class Node:
        def __init__(self, data):
            self.data = data
            self.esquerda = None
            self.direita = None

        def __str__(self):
            return str(self.data)

    class BinaryTree:
        def __init__(self, data):
            node = Node(data)
            self.root = Node(data)

    if __name__ == "__main__":
        if rank1 >= rank2 >= rank3:
            tree = BinaryTree(rank1)
            tree.root.direita = Node(rank2)
            tree.root.esquerda = Node(rank3)
            print('\n 1° -', play1,"Pontos:", tree.root)
            print("  2° -",play2,"Pontos:",tree.root.direita)
            print("   3° -",play3,"Pontos:",tree.root.esquerda)
        elif rank2 >= rank1 >= rank3:
            tree = BinaryTree(rank2)
            tree.root.direita = Node(rank1)
            tree.root.esquerda = Node(rank3)
            print("\n1° -", play2, "Pontos:", tree.root.direita)
            print("  2° -",play1, "Pontos: ",tree.root)
            print("   3° -", play3, "Pontos",tree.root.esquerda)
            print("")
        elif rank2 >= rank3 >= rank1:
            tree = BinaryTree(rank2)
            tree.root.direita = Node(rank3)
            tree.root.esquerda = Node(rank1)
            print("\n1° -", play2, "Pontos:", tree.root.direita)
            print("  2° -", play3, "Pontos: ", tree.root.esquerda)
            print("   3° -", play1, "Pontos", tree.root)
            print("")
        elif rank3 >= rank2 >= rank1:
            tree = BinaryTree(rank3)
            tree.root.direita = Node(rank2)
            tree.root.esquerda = Node(rank1)
            print("\n1° -", play3, "Pontos:", tree.root.direita)
            print("  2° -", play2, "Pontos: ", tree.root.esquerda)
            print("   3° -", play1, "Pontos", tree.root)
            print("")
        elif rank3 >= rank1 >= rank2:
            tree = BinaryTree(rank3)
            tree.root.direita = Node(rank1)
            tree.root.esquerda = Node(rank2)
            print("\n1° -", play3, "Pontos:", tree.root.direita)
            print("  2° -", play1, "Pontos: ", tree.root)
            print("   3° -", play2, "Pontos", tree.root.esquerda)
            print("")
        elif rank1 >= rank3 >= rank2:
            tree = BinaryTree(rank1)
            tree.root.direita = Node(rank3)
            tree.root.esquerda = Node(rank2)
            print("\n1° -", play1, "Pontos:", tree.root)
            print("  2° -", play3, "Pontos: ", tree.root.direita)
            print("   3° -", play2, "Pontos", tree.root.esquerda)
            print("")
        else:
            tree = BinaryTree(rank1)
            tree.root.direita = Node(rank2)
            tree.root.esquerda = Node(rank3)
            print("\n", play1, play2,"e", play3, "terminou empatados com",tree.root, "pontos")


def jogador1():
    lista_palavras = ['vaca', 'cavalo', 'coruja', 'lula', 'abelha', 'camelo', 'elefante', 'baleia', 'besouro','cachorro',
                      'coala', 'formiga', 'galinha', 'galo', 'pinto', 'pombo', 'andorinha']  # criação de uma lista
    palavras = lista_palavras[randint(0, len(lista_palavras) - 1)]  # separar uma palavra aleatóriamentede 0 até o tamanho da lista
    lista_letras = list(palavras)  # receber a palavra aleatória partida em letras.
    vidas1 = 5  # número de vidas1
    sublinhadas = []  # a lista onde vai receber os valores digitados
    win = False  # criei só pra usar condição
    rodada = 0
    rodada1 = 0
    rodada2 = 0
    rodada3 = 0
    nome1 = input(str('         Digite seu nome: '))
    print('\n\n           웃 JOGO DA FORCA 웃\n')
    print(' A cada rodada que passa seus pontos vai se somando\nE na medida que você erra, vai desvalorizando a palavra\n')
    print('             Sobre: Animais\n')
    print(' \n')

    for i in range(0, len(lista_letras)):  # adicionar as sub-linhas na lista: sublinhadas
        sublinhadas.append('_')

    while not win and vidas1 != 0:  # enquanto vidas1 for diferente de 0 e win for false faça:

        amostra = ""  # criei só pra separar as sub-linhas
        ultimoChar = ""  # criei só pra quando o cara repetir a letra.
        for i in sublinhadas:
            amostra = amostra + " " + i  # seprar as sub-linhas pra n ficar >> ______
        print('Pontos = ' + str(vidas1) + ' Palavra a ser adivinhada: ' + amostra)  # Mostrando o número de vidas1 e de letras da palavra.
        falhou = False  # Criei só pra diminuir a vida do cara
        letra = input(str('Digite uma letra: '))

        for i in range(0, len(lista_letras)):
            if letra == lista_letras[i]:  # Se o caractere q botaram for igual a palavra, ele vai botar no lugar da sub-linha a letra.
                sublinhadas[i] = letra
                ultimoChar = letra
                falhou = False
            elif ultimoChar == "":
                falhou = True

        if falhou:  # Se ele falhou a vida dele diminui em - 1 e se chegar a zero o while para.
            vidas1 -= 1
            if vidas1 == 4:
                print('                O  ')
            elif vidas1 == 3:
                print('                O  ', '\n               /|  ')
            elif vidas1 == 2:
                print('                O  ', '\n               /|\ ')
            elif vidas1 == 1:
                print('                O  ', '\n               /|\ ', '\n               /   ')
            elif vidas1 == 0:
                print('                O  ', '\n               /|\ ', '\n               / \ \n')

        if sublinhadas == lista_letras:
            print("\nParabéns você acertou a palavra !!\n")
            rodada += 1
            if rodada == 1:
                sublinhadas.clear()  # Vai limpar digitou na lista sublinhadas
                palavras = lista_palavras[
                    randint(0, len(lista_palavras) - 1)]  # vai separar novamente um item aleatorio
                lista_letras = list(palavras)  # e vai jogar novamente na lista_letras
                for i in range(0, len(lista_letras)):  # Vai adicionar as sub-linhas novamente
                    sublinhadas.append('_')

                    rodada1 = vidas1

            elif rodada == 2:
                sublinhadas.clear()  # Vai limpar digitou na lista sublinhadas
                palavras = lista_palavras[
                    randint(0, len(lista_palavras) - 1)]  # vai separar novamente um item aleatorio
                lista_letras = list(palavras)  # e vai jogar novamente na lista_letras
                for i in range(0, len(lista_letras)):  # Vai adicionar as sub-linhas novamente
                    sublinhadas.append('_')

                    rodada2 = vidas1

            elif rodada == 3:
                sublinhadas.clear()  # Vai limpar digitou na lista sublinhadas
                palavras = lista_palavras[
                    randint(0, len(lista_palavras) - 1)]  # vai separar novamente um item aleatorio
                lista_letras = list(palavras)  # e vai jogar novamente na lista_letras
                for i in range(0, len(lista_letras)):  # Vai adicionar as sub-linhas novamente
                    sublinhadas.append('_')

                    rodada3 = vidas1

            else:
                win = True
    if vidas1 == 0:
        lista_letras = ''.join(map(str, lista_letras))  # deixar as letras direitinha :D
        print('\nPoxa você foi ✞ enforcado ✞, o animal era:', lista_letras)
        rodada += 1
        if rodada == 1:
            sublinhadas.clear()  # Vai limpar digitou na lista sublinhadas
            palavras = lista_palavras[
                randint(0, len(lista_palavras) - 1)]  # vai separar novamente um item aleatorio
            lista_letras = list(palavras)  # e vai jogar novamente na lista_letras
            for i in range(0, len(lista_letras)):  # Vai adicionar as sub-linhas novamente
                sublinhadas.append('_')

                rodada1 = vidas1

        elif rodada == 2:
            sublinhadas.clear()  # Vai limpar digitou na lista sublinhadas
            palavras = lista_palavras[
                randint(0, len(lista_palavras) - 1)]  # vai separar novamente um item aleatorio
            lista_letras = list(palavras)  # e vai jogar novamente na lista_letras
            for i in range(0, len(lista_letras)):  # Vai adicionar as sub-linhas novamente
                sublinhadas.append('_')

                rodada2 = vidas1

        elif rodada == 3:
            sublinhadas.clear()  # Vai limpar digitou na lista sublinhadas
            palavras = lista_palavras[
                randint(0, len(lista_palavras) - 1)]  # vai separar novamente um item aleatorio
            lista_letras = list(palavras)  # e vai jogar novamente na lista_letras
            for i in range(0, len(lista_letras)):  # Vai adicionar as sub-linhas novamente
                sublinhadas.append('_')

                rodada3 = vidas1

        else:
            pass
    vidas1 = (rodada1 + rodada2 + rodada3)
    return vidas1, nome1

game = float(input('Jogar com 1, 2 ou 3 jogadores ? ? 1/2/3: '))
if game ==  1:
    rank1, play1 = jogador1()
elif game == 2:
    rank1, play1 = jogador1()
    rank2, play2 = jogador1()
    arvore()
else:
    rank1, play1 = jogador1()
    rank2, play2 = jogador1()
    rank3, play3 = jogador1()
    arvore2()

recomeço = False
while not recomeço:
    resetar = input(str('\nJogar novamente ? s/n '))
    if resetar == 's':
        game = float(input('Jogar com 1, 2 ou 3 jogadores ? ? 1/2/3: '))
        if game == 1:
            rank1, play1 = jogador1()
        elif game == 2:
            rank1, play1 = jogador1()
            rank2, play2 = jogador1()
            arvore()
        else:
            rank1, play1 = jogador1()
            rank2, play2 = jogador1()
            rank3, play3 = jogador1()
            arvore2()

    else:
        recomeço = True