# Apos iniciar o programa começamos
# mostra uma mensagem de boas-vindas
print("\n" + "="*70)
print("Boas - Vindas para jogar o jogo do adivinha por favor nos diga seu nome")
print("="*70 + "\n")

nome = input(" por favor nos diga seu nome: ")

# limpa o pront 
import os
os.system(' cls ' if os.name == 'nt' else 'clear')

# exibir o nome bonitinho do jogador

print("\n" + "-"*30)
print(f"    Bem-vindo(a), {nome}!")
print("-"*30 + "\n")

# mostra as regras
print("\n" + "="*32) # serve para adicionar colunas de === em cima da frase, ajuda na estetica do game
print("  Agora vamos te dizer as regras! ")
print("="*32 + "\n")
print("\n" + "="*28)
print("nao burla os codigos do game")
print("="*28 + "\n")
print("\n" + "="*45)
print("nao pode esgotar o seu limite de tentativas")
print("="*45 + "\n")

print(" agora vamos la voce tem 100 pontos ")

print("\n" + "-"*30)
print("100 Pontos")
print("-"*30 + "\n")

print("como agradecimento de boas vindas")
print("vamos te dar 100 ponto de bonus")

pontos=int(input("Digite o valor dos pontos:"))
print(pontos)
soma = pontos + 100

if pontos <= 50:
                 print("seus pontos foram pra:" , soma)
else:
              print("valor invalido> fim de jogo!")
              import os 
              os.system(' cls ' if os.name == 'nt' else 'clear')

# começando 
print("\n" + "="*27)
print(" agora vamos começar")
print("="*27 + "\n")

sim = input(" esta pronto? para começar digite sim : ")

# limpa o pront 
import os
os.system(' cls ' if os.name == 'nt' else 'clear')
# começo do jogo adivinha
import random

ranking = {}

def mostrar_nome_do_jogo():
    print("Bem-vindo ao Jogo do Número Mágico!")

def solicitar_nome_jogador():
    nome_jogador = input("Digite o seu nome: ")
    return nome_jogador

def jogo(nome_jogador):
    numero_magico = random.randint(1, 100)
    tentativas = 7

    while tentativas > 0:
        numero_digitado = int(input("Tentativa {}: Digite um número entre 1 e 100: ".format(7 - tentativas)))

        if numero_digitado < numero_magico:
            print("O número digitado é menor que o número mágico!")
        elif numero_digitado > numero_magico:
            print("O número digitado é maior que o número mágico!")
        else:
            print("Parabéns, {}! Você acertou o número mágico em {} tentativas!".format(nome_jogador, 7 - tentativas))
            ranking[nome_jogador] = 7 - tentativas
            return

        tentativas -= 1

    print("Infelizmente, {}! Você não conseguiu acertar o número mágico. O número correto era {}.".format(nome_jogador, numero_magico))

def mostrar_ranking():
    print("\nRanking:")
    for jogador, pontuacao in sorted(ranking.items(), key=lambda x: x[1]):
        print("{}: {} tentativas".format(jogador, pontuacao))

def main():
    mostrar_nome_do_jogo()
    while True:
        nome_jogador = solicitar_nome_jogador()
        jogo(nome_jogador)
        mostrar_ranking()
        resposta = input("\nDeseja jogar novamente? (s/n): ")
        if resposta.lower() != 's':
            break

if __name__ == "__main__":
    main()
