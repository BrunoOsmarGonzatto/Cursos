# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:10:55 2024

@author: bruno
"""

def escolha ():
    
    print("\nBem vindo ao jogo do NIM!\n\n *Você conhece o jogo do NIM? Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro. Dois jogadores jogam alternadamente, retirando pelo menos 1 e no máximo m peças cada um. Quem tirar as últimas peças possíveis ganha o jogo.*\n")
    print("Escolha: \n\n","1 - para jogar uma partida isolada\n", "2 - para jogar um campeonato", end=" ")
    
    loop = True
    while loop:
        escolha = int(input(""))
        if escolha == 1:
            print("\nVocê escolheu partida isolada!")
            return 1
            loop = False
        else:
            if escolha == 2:
                print("\nVocê escolheu campeonato!")
                return 3
                loop = False
            else:
                print("\nEscolha uma opção válida:", end=" ")
                
def computador_escolhe_jogada (n,m):
    j = 1
    peças = 0
    while n % (m+1) != 0 and j <= m:
        n -= j
        peças = peças + j
        
    if peças == 1:
        print ("\nO computador tirou uma peça.")
    else:
        print ("\nO computador tirou", peças, "peças.")
    return peças

def usuario_escolhe_jogada (n,m):
    aux = True
    while aux:
        jogada_usu = int(input("\nQuantas peças você vai tirar? "))
        if jogada_usu > m or jogada_usu <= 0 or jogada_usu > n:
            print ("\nOops! Jogada inválida! Tente de novo.")
        else:
            n -= jogada_usu
            aux = False
    
    if jogada_usu == 1:
        print ("\nVocê tirou uma peça.")
    else:
        print ("\nVocê tirou", jogada_usu, "peças.")
    return jogada_usu
	
def partida ():
    fail_safe = False
    while not fail_safe:
        n = int(input("\nQuantas peças no tabuleiro? "))
        m = int(input("Limite de peças retiradas por jogada? "))
        if n < m or n <=0 or m <=0:
            print("\nJogo impossível. Insira novamente.")
        else:
            fail_safe = True
    
    if n % (m+1) == 0:
        print ("\nVocê começa!")
        vez = -1
    else:
        print ("\nComputador começa!")
        vez = -2
    
    while n != 0:
        while vez == -1:
            n -= usuario_escolhe_jogada(n, m)
            if n == 0:
                print("Fim do jogo! Você ganhou!")
                vez = 0
                placar = True
            else:                
                if n == 1:
                    print ("Agora resta apenas uma peça no tabuleiro.")
                else:
                    print ("Agora restam", n,"peças no tabuleiro.")
                n -= computador_escolhe_jogada(n, m)
                if n == 0:
                    print("Fim do jogo! O computador ganhou!")
                    vez = 0
                    placar = False
                else:                
                    if n == 1:
                        print ("Agora resta apenas uma peça no tabuleiro.")
                    else:
                        print ("Agora restam", n,"peças no tabuleiro.")
        while vez == -2:
            n -= computador_escolhe_jogada(n, m)
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                vez = 0
                placar = False
            else:                
                if n == 1:
                    print ("Agora resta apenas uma peça no tabuleiro.")
                else:
                    print ("Agora restam", n,"peças no tabuleiro.")
                n -= usuario_escolhe_jogada(n, m)
                if n == 0:
                    print("Fim do jogo! Você ganhou!")
                    vez = 0
                    placar = True
                else:                
                    if n == 1:
                        print ("Agora resta apenas uma peça no tabuleiro.")
                    else:
                        print ("Agora restam", n,"peças no tabuleiro.")
    
    if placar:
        return placar
    else:
        return placar

def campeonato ():
    i = 1
    pontos_usu = 0
    pontos_comp = 0
    
    while i < 4:
        print ("\n**** Rodada", i, "****")
        if partida() == True:
            pontos_usu += 1
        else:
            pontos_comp += 1
        i += 1
    
    return print("\n**** Final do campeonato! ****\n\nPlacar: Você", pontos_usu,"X",pontos_comp,"Computador")

################################################################################################################
jogo_repetir = " "
jogo = True
while jogo:
    if escolha() == 1:
        partida()
        
        loop = True
        while loop:
            jogo_repetir = str.lower(input("\nRepetir o jogo? [s] [n]: "))
            if jogo_repetir == "s":
                jogo = True
                loop = False
            else:
                if jogo_repetir == "n":
                    jogo = False
                    loop = False
                else:
                    print("\nEscolha uma opção válida.")
    else:
        campeonato()
        
        loop = True
        while loop:
            jogo_repetir = str.lower(input("\nRepetir o jogo? [s] [n]: "))
            if jogo_repetir == "s":
                jogo = True
                loop = False
            else:
                if jogo_repetir == "n":
                    jogo = False
                    loop = False
                else:
                    print("\nEscolha uma opção válida.")