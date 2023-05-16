#1. Crie um algoritmo que receba um valor em metros e converta para centímetros]


def exercico_um ():
    metros = float(input('digite o valor em metros\n'))
    print('esse é o valor em centimetros')

def metros_para_cm (metros):
    return metros * 100

#2. . Crie um algoritmo que pergunte quanto você ganha por hora e o número de horas que você trabalha por mês, o algoritmo deve calcular e mostrar qual seu salário naquele mês.
def exercicio_dois():
    pagar = int(input('digite o quanto voce ganha por hora\n'))
    hrs = int(input('digite o quantas horas voce trabalha por mes\n'))

    salario = (pagar*hrs)
    print(f"o seu salario no mes de março será:\n{salario}")

def salario_hora (salario):
    return salario * 1 
    #Crie um algoritmo que receba uma temperatura em Fahrenheit e converta para Celsius, utilizando a fórmula:

#tempCelsius = 5 * ((tempFahren-32) / 9)
def exercico_tres():
    farm = int(input('indique a temperatura em Fahrenheit:\n'))
    tempCelsius = 5 * ((farm-32) / 9)
    print(tempCelsius)

#Crie um algoritmo que receba a altura e o peso de uma pessoa e mostre seu Índice de Massa Corporal (IMC), utilizando a seguinte fórmula:
def exercicio_quatro():
    peso = float(input('digite seu peso (kg)\n'))
    altura = float(input('digite sua altura (m)\n'))
    imc = peso/(altura *2)
    print(f"seu imc é:{imc:.3f}")

#5. Zé Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar 
#o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes 
#maior que o estabelecido pelo regulamento de pesca do estado de São Paulo 
#(30 quilos) deve pagar uma multa de R$ 3,00 por
# quilo excedente. Zé precisa que você faça um algoritmo que leia a variável
# peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a
# quantidade de quilos além do limite e na variável multa o valor da multa
# que Zé deverá pagar. Imprima os dados do algoritmo com as mensagens
# adequadas.

def exercicio_cincun():
    peixeT = float(input("qual o peso total do peixe?"))

    if peixeT < 30:
        print("Sem taxa")
    else:
        peixeT=peixeT-30
        multa= 3 * peixeT
        print(f'pagar taxa {multa}')

#6. Crie um algoritmo que receba quanto você ganha por hora e quantas horas trabalhou no mês. O algoritmo deve calcular e mostrar o seu salário
#no referido mês, sabendo que serão descontados 11% do Imposto de Rende (IR) e mais 8% do INSS. No final o algoritmo deve apresentar:
#a. Salário bruto
#b. Valor do imposto de renda
#c. Valor do INSS
#d. Salário líquido (líquido = bruto – impostos)
def exercicio_seix():
    pagar = int(input('digite o quanto voce ganha por hora\n'))
    hrs = int(input('digite o quantas horas voce trabalha por mes\n'))

    salario = (pagar*hrs)
    print(f"o seu salario no mes de março será:\n{salario}")

    iRs = (salario * 0.11)
    iR = (salario - iRs)
    iNS = (salario * 0.08)
    iNSS = (salario - iNS)
    liquido = (salario - iRs - iNS)

    print(f"A: Seu salario bruto é:\n {salario}\n2")
    print(f"B: Valor do imposto de renda:\n {iRs}\n2")
    print(f"C: O valor do INSS é:\n {iNS}")
    print(f"D: O salario liquido é:\n {liquido:.2f}")

#aaaaaaaaaaaa

#15.Você̂ foi contratado por uma grande indústria da sua cidade para auxiliar o
#RH com o desenvolvimento de um software, a empresa foi comprada por um
#grande grupo internacional, isso foi uma boa notícia para todos os
#funcionários pois irão receber um aumento. O seu papel como desenvolvedor
#é criar um programa que irá ajudar o RH a calcular os reajustes. Para
#desenvolver você̂ precisa saber de algumas regras, todos os funcionários irão
#receber algum aumento, mas essa porcentagem vai variar conforme as faixas
#salariais da seguinte forma:
#o salários até R$ 800,00: aumento de 20%
#o salários acima de R$ 800,00 até R$ 1300,00: aumento de 15%
#o salários acima de R$ 1300,00 e R$ 2500,00: aumento de 10%
#o salários de R$ 2500,00 em diante: aumento de 5%
#Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

def exercicio_sete():
    a = float(input("Qual o seu salario?\n"))

    if a < 800.00 :
        valor_a = a * 0.2
        valor_aa = a + valor_a
        print(f"Valor inicial {a}\nValor com aumento {valor_a}\nValor agora {valor_aa}")
    elif a > 800.01 and a < 1300.00 :
        valor_b = a * 0.15
        valor_ab = a + valor_b
        print(f"Valor inicial {a}\nValor com aumento {valor_b}\nValor agora {valor_ab}")
    elif a > 1300.01 and a < 2500.00 :
        valor_c = a * 0.1
        valor_ac = a + valor_c
        print(f"Valor inicial {a}\nValor com aumento {valor_c}\nValor agora {valor_ac}")
    elif a > 2500.01:
        valor_d = a * 0.05
        valor_ad = a + valor_d
        
    print(f"Valor inicial {a}\nValor com aumento {valor_d}\nValor agora {valor_ad}")

