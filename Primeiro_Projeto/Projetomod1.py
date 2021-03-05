# Apresentação do tema, alunos e titulo do jogo
print("*"*105)
print("Trabalho de conclusão do módulo 1 do curso VamoAi")
print()
print("Tema - Vida de Programador")
print()
print("Alunos:\n"
      "Jheysson Douglas\n"
      "Jennifer Stefani\n"
      "Natalia Gomes\n"
      "Maressa Machado\n"
      "Aline Santos\n")
print()
print("Projeto de Jheysson Douglas")
print()
print("*"*105)
print("**************************************** JOGO DO DIMAS **************************************************")
print()
print("Bem vindos ao Jogo do Dimas em vida de programador.")
print()

# Explicando como o jogo funciona
print("Nesse jogo três jogadores disputam juntos um Quiz de multipla escolha\n"
      "passando por 3 cenários diferentes\n"
      "e, no final ,caso alcancem a pontuação mínima,\n"
      "vão ter a chance de abrir uma porta e saber \n"
      "se ganharam o prêmio máximo, ou não.")

print()

print("Cenários:\n"
      "Serão 3 cenários diferentes:\n"
      "Fáceis, Médios e Difíceis")

print()

print("Jogadores:\n"
      "Três jogadores diputando juntos para no final \n"
      "levarem o prêmio máximo para casa, ou não :)")

print()

print("O Quiz:\n"
      "Serão 15 perguntas de multipla escolha referentes a programação,\n"
      "Distribuídas da seguinte forma:\n"
      "5 de nível fácil, 5 de nível médio e 5 de nível difícil.\n"
      "Vocês vão receber as perguntas e\n"
      "discutirem entre os três para poder chegar numa resposta.\n"
      "A cada resposta correta vocês marcam 10 pontos,\n"
      "A cada resposta errada vocês ficam zerados.")

print()

print("Pontuação mínima para chegar ate a porta:\n"
      "120 pontos, ou seja, vocês precisam acertar doze\n"
      "das quinze questões para avançarem ate a porta.")

print()

print("Se acertarem o mínimo das perguntas:\n"
      "Vocês vão ter a oportunidade de escolher entre seis portas.\n"
      "Duas tem o prêmio máximo, duas dão a possibilidade de vocês\n"
      "voltarem para jogar novamente e as outras duas \n"
      "excluem vocês do meu jogo.")

print()

print("Se não acertarem o mínimo das perguntas:\n"
      "O jogo termina automaticamente pra vocês!")

print()
# premiação do jogo + inicio do codigo
print("Prêmio Máximo: R$50.000,00")
print("Distribuídos entre os três")
print()
print("*"*105)
print("E aí, Preparados? ")
print()
comecar = input("Aperte ENTER para começar!")
print(comecar)

print
print("*"*105)


# CONHECENDO OS PERSONAGENS
jogador1 = input(str("Jogador 1, qual seu nome? "))
cidade1 = input(str("De qual cidade você fala? "))
jogador1 = jogador1.upper()
print("Ok", jogador1, "seus dados ja estão Salvos!")
cidade1 = cidade1.upper()

print("*"*105)

jogador2 = input(str("Jogador 2, qual seu nome? "))
cidade2 = input(str("De qual cidade você fala? "))
jogador2 = jogador2.upper()
print("Ok", jogador2, "seus dados ja estão Salvos!")
cidade2 = cidade2.upper()

print("*"*105)

jogador3 = input(str("Jogador 3, qual seu nome? "))
cidade3 = input(str("De qual cidade você fala? "))
jogador3 = jogador3.upper()
print("Ok", jogador3, "seus dados ja estão Salvos!")
cidade3 = cidade3.upper()

print("*"*105)

print()

print("Atenção", jogador1, ",", jogador2, "e",
      jogador3, "nós vamos começar nosso jogo!")
print(input("Pressione ENTER para iniciar!"))
print()
print("*"*105)


def perguntas():
    ##### COMEÇO DAS PERGUNTAS #######
    ######## PERGUNTA 1 ############
    print("Cenário 1: Nível Fácil")
    pontos = 0
    print("*"*105)
    print()
    print("Pergunta número 1: ")
    print()
    print("Qual a função do print? \n"
          "[1] Serve para somar dois valores.\n"
          "[2] O print faz a quebra de linhas dentro de um texto.\n"
          "[3] print não é utilizado em Python\n"
          "[4] A grosso modo a função print() serve para imprimir os argumentos passados a ela no terminal.")
    print()
    pergunta1 = int(input("Qual a resposta correta? "))
    print()
    if pergunta1 == 4:
        print("Certa Resposta!")
        print("Vocês marcaram 10 pontos")
        pontos = pontos + 10
    else:
        print("Vocês erraram!")
    print()
    print("*"*105)
    print()

    # Pergunta 2
    print("Pergunta número 2: ")
    print()
    print("Qual dessas palavras é uma palavra reservada?\n"
          "[1] carro\n"
          "[2] continue\n"
          "[3] atividade\n"
          "[4] item")
    print()
    pergunta2 = int(input("Qual a resposta correta? "))
    print()
    if pergunta2 == 2:
        print("Certa Resposta!")
        print("Vocês marcaram 10 pontos")
        pontos = pontos + 10
    else:
        print("Vocês erraram!")

    print()
    print("*"*105)
    print()

    # Pergunta 3
    print("Pergunta número 3: ")
    print()
    print("O que é uma Variável? \n"
          "[1] Um nome que se refere a um valor\n"
          "[2] Um dos valores que um operador produz\n"
          "[3] Uma sequencia de comandos que executam uma tarefa\n"
          "[4] Conjunto de regras e procedimentos")
    print()
    pergunta3 = int(input("Qual a resposta correta? "))
    print()
    if pergunta3 == 1:
        print("Certa Resposta!")
        print("Vocês marcaram 10 pontos")
        pontos = pontos + 10
    else:
        print("Vocês erraram!")
    print()
    print("*"*105)
    print()

    # Pergunta 4
    print("Pergunta número 4: ")
    print()
    print("Sobre algoritmos, escolha a opção correta: \n"
          "[1] São palavras reservadas dentro de um código.\n"
          "[2] Verifica se dois valores são iguais.\n"
          "[3] Uma sequencia finita de regras, raciocinios que permitem chegar a uma solução.\n"
          "[4] Separa as palavras dentro de uma variável.")
    print()
    pergunta4 = int(input("Qual a resposta correta? "))
    print()
    if pergunta4 == 3:
        print("Certa Resposta!")
        print("Vocês marcaram 10 pontos")
        pontos = pontos + 10
    else:
        print("Vocês erraram!")
    print()
    print("*"*105)
    print()

    # Pergunta 5
    print("Pergunta número 5: ")
    print()
    print("Uma linguagem de programação de alto nível e interpretada. Essa frase se\n"
          "refere a qual linguagem de programação? \n"
          "[1] Python\n"
          "[2] Java Script\n"
          "[3] C++\n"
          "[4] Java")
    print()
    pergunta5 = int(input("Qual a resposta correta? "))
    print()
    if pergunta5 == 1:
        print("Certa Resposta!")
        print("Vocês marcaram 10 pontos")
        pontos = pontos + 10
    else:
        print("Vocês erraram!")
    print()
    print("*"*105)


######## CENÁRIO 2 ##########
######## PERGUNTA 1 ##########
    print("Cenário 2: Nível Médio")
    print("*"*105)
    print()
    print("Pergunta número 1: ")
    print()
    print("Para que serve o método .upper() :\n"
          "[1] Serve para diminuir um valor.\n"
          "[2] Serve para somar um valor. \n"
          "[3] Serve para deixar as letras Minusculas.\n"
          "[4] Serve para deixar as letras Maiusculas.")
    print()
    pergunta1 = int(input("Qual a resposta correta? "))
    print()
    if pergunta1 == 4:
        print("Certa Resposta!")
        print("Vocês marcaram 10 pontos")
        pontos = pontos + 10
    else:
        print("Vocês erraram!")
    print()
    print("*"*105)
    print()

    # Pergunta 2
    print("Pergunta número 2: ")
    print()
    print("Para que serve o método .append() dentro de listas:  \n"
          "[1] Pular linha.\n"
          "[2] Adicionar um novo elemento no final da lista.\n"
          "[3] Remover uma palavra.\n"
          "[4] Estender a lista com a sequência.")
    print()
    pergunta2 = int(input("Qual a resposta correta? "))
    print()
    if pergunta2 == 2:
        print("Certa Resposta!")
        print("Vocês marcaram 10 pontos")
        pontos = pontos + 10
    else:
        print("Vocês erraram!")

    print()
    print("*"*105)
    print()

    # Pergunta 3
    print("Pergunta número 3: ")
    print()
    print("Para que serve o método .clear() dentro de listas:  \n"
          "[1] Remove todos os elementos da lista.\n"
          "[2] Retorna dois valores.\n"
          "[3] Insere comandos dentro de uma função.\n"
          "[4] Não existe esse elemento dentro de listas.")
    print()
    pergunta3 = int(input("Qual a resposta correta? "))
    print()
    if pergunta3 == 1:
        print("Certa Resposta!")
        print("Vocês marcaram 10 pontos")
        pontos = pontos + 10
    else:
        print("Vocês erraram!")
    print()
    print("*"*105)
    print()

    # Pergunta 4
    print("Pergunta número 4: ")
    print()
    print("Para que serve o método .reverse():\n"
          "[1] Retornar a quantidade de ocorrências de um elemento na lista.\n"
          "[2] Verifica se tem alguma palavra incorreta.\n"
          "[3] Reverter a ordem dos elementos na lista.\n"
          "[4] Separar as palavras dentro de uma lista.")
    print()
    pergunta4 = int(input("Qual a resposta correta? "))
    print()
    if pergunta4 == 3:
        print("Certa Resposta!")
        print("Vocês marcaram 10 pontos")
        pontos = pontos + 10
    else:
        print("Vocês erraram!")
    print()
    print("*"*105)
    print()

    # Pergunta 5
    print("Pergunta número 5: ")
    print()
    print("Para que serve o método .sort() :\n"
          "[1] Ordena a lista.\n"
          "[2] Limpa toda a lista.\n"
          "[3] Faz o sorteio de nomes.\n"
          "[4] Remove um elemento da lista.")
    print()
    pergunta5 = int(input("Qual a resposta correta? "))
    print()
    if pergunta5 == 1:
        print("Certa Resposta!")
        print("Vocês marcaram 10 pontos")
        pontos = pontos + 10
    else:
        print("Vocês erraram!")
    print()
    print("*"*105)

##########  CENARIO 3  ##########
########## PERGUNTA 1 ###########
    print("Cenário 3: Nível Difícil")
    print("*"*105)
    print()
    print("Pergunta número 1: ")
    print()
    print("Qual a função da estrutura de repetição? \n"
          "[1] São estruturas capazes de destruir um código.\n"
          "[2] Fazem a sintaxe do código. \n"
          "[3] Em Python não existe repetição.\n"
          "[4] São utilizadas para repetir a execução de algum bloco de código no programa.")
    print()
    pergunta1 = int(input("Qual a resposta correta? "))
    print()
    if pergunta1 == 4:
        print("Certa Resposta!")
        print("Vocês marcaram 10 pontos")
        pontos = pontos + 10
    else:
        print("Vocês erraram!")
    print()
    print("*"*105)
    print()

    # Pergunta 2
    print("Pergunta número 2: ")
    print()
    print("Qual dessas palavras é um comando de repetição que podemos utilizar em nosso código? \n"
          "[1] White\n"
          "[2] While\n"
          "[3] Def\n"
          "[4] Return")
    print()
    pergunta2 = int(input("Qual a resposta correta? "))
    print()
    if pergunta2 == 2:
        print("Certa Resposta!")
        print("Vocês marcaram 10 pontos")
        pontos = pontos + 10
    else:
        print("Vocês erraram!")

    print()
    print("*"*105)
    print()

    # Pergunta 3
    print("Pergunta número 3: ")
    print()
    print("O que significa Iterar uma sequencia? \n"
          "[1] Acessar todos os elementos de uma sequência.\n"
          "[2] Multiplicar uma sequencia.\n"
          "[3] Passar para outro bloco de códigos.\n"
          "[4] Elaborar formas de pular execução do código.")
    print()
    pergunta3 = int(input("Qual a resposta correta? "))
    print()
    if pergunta3 == 1:
        print("Certa Resposta!")
        print("Vocês marcaram 10 pontos")
        pontos = pontos + 10
    else:
        print("Vocês erraram!")
    print()
    print("*"*105)
    print()

    # Pergunta 4
    print("Pergunta número 4: ")
    print()
    print("Qual a função do comando break? \n"
          "[1] Modificar todo o código.\n"
          "[2] Fazer a leitura do código.\n"
          "[3] Interromper toda a iteração.\n"
          "[4] Separar os blocos do código.")
    print()
    pergunta4 = int(input("Qual a resposta correta? "))
    print()
    if pergunta4 == 3:
        print("Certa Resposta!")
        print("Vocês marcaram 10 pontos")
        pontos = pontos + 10
    else:
        print("Vocês erraram!")
    print()
    print("*"*105)
    print()

    # Pergunta 5
    print("Pergunta número 5: ")
    print()
    print("Para que serve o comando range ? \n"
          "[1] Serve para realizar uma iteração através de números.\n"
          "[2] Serve para saltar linhas.\n"
          "[3] Serve para concluir nosso bloco de códigos.\n"
          "[4] Serve para realizar a impressão(print) dentro do nosso código")
    print()
    pergunta5 = int(input("Qual a resposta correta? "))
    print()
    if pergunta5 == 1:
        print("Certa Resposta!")
        print("Vocês marcaram 10 pontos")
        pontos = pontos + 10
    else:
        print("Vocês erraram!")
    print()
    print("*"*105)

    # Pontuação final
    print("A pontuação final de vocês é:", int(pontos), "pontos")

    print("*"*105)
    print()

    # Condições
    if pontos >= 120:
        print("Show de bola", jogador1, ",", jogador2, ", e", jogador3, "!")
        print()
        print("*"*105)
        print()
        print("Como vocês alcançaram a pontuação no jogo, agora vocês terão a oportunidade de abrir\n"
              "uma das 6 portas para descobrirem o valor do Prêmio de vocês!")
        print()
        print("*"*105)
        print()
        print("Escolha uma das 6 portas: ")
        print("[1] Porta 1")
        print("[2] Porta 2")
        print("[3] Porta 3")
        print("[4] Porta 4")
        print("[5] Porta 5")
        print("[6] Porta 6")
        resposta = int(input("Qual Porta vocês escolhem? "))
        print()
        print("*"*105)

        if resposta == 1 or resposta == 3:
            print()
            print("Infelizmente vocês nao ganharam nada :(")
            print()

        elif resposta == 2 or resposta == 5:
            print()
            print("Shoooooooow, PORTA CERTA. Vocês vão levar para casa\n"
                  "o prêmio máximo no valor de R$50.000,00")
            print()
            print("*"*105)
            print()
            print(jogador1, "você leva pra", cidade1, " o valor de R$16.666,66")
            print(jogador2, "você leva pra", cidade2, " o valor de R$16.666,66")
            print(jogador3, "você leva pra", cidade3, " o valor de R$16.666,66")
            print()

        elif resposta == 4 or resposta == 6:
            print()
            print("Infelizmente Vocês nao ganharam o prêmio. Mas poderão jogar novamente e tentar ganhar o prêmio máximo!")
            print()
            print("*"*105)
            print()
            print("Querem jogar novamente? ")
            print()
            
            jogarnovamente = "S"
            while(jogarnovamente.upper() == "S"):
                print("Jogar novamente? S ou N")
                jogadenovo = input("Digite a opção: ")
                if jogadenovo.upper() == "S":
                    jogadenovo == perguntas()
                    print("*"*105)
                else:
                    print("Fim de Jogo")
                    break
    # Caso não acertem o mínimo de 120 pontos, já vão cair aqui
    else:
        print()
        print("Infelizmente vocês não atingiram o valor necessário para disputar o prêmio!")
        print()
    print("*"*105)


perguntas()
