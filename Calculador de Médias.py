import time
import math
import decimal

time.sleep(1)
print("Olá! Bem vindo ao Calculador de Médias! Este programa foi criado por: ")
print("")
print("                                                           |--------------------------------------------------------|")
print("                                                           |                                                        |")
print("                                                           |    -------               ---------     |---------      |")
print("                                                           |       |      |       |   |             |        |      |")
print("                                                           |       |      |       |   |             |        |      |")
print("                                                           |       |      |       |   |     ----|   |--------|      |")
print("                                                           |       |      |       |   |         |   |        |      |")
print("                                                           |       |      ---------   -----------   |        |      |")
print("                                                           |                                                        |")
print("                                                           |  © TUGA 2020                                @tugauga   |")
print("                                                           |--------------------------------------------------------|")
print("")
time.sleep(2)
print("---------------------------------------------------------------------------------------------------------------------")
print("Bem, vamos a isto!")
time.sleep(1)

# Inputs possíveis de sim ou não
sim = ["s","S","sim","SIM","Sim","sIm","siM","SIm","sIM"]
nao = ["n","N","nao","NAO","Nao","nAo","naO","NAo","nAO","não","NÃO","Não","nÃo","nãO","NÃo","nÃO"]
sn = sim + nao

# Função que arredonda uma nota (19.4 é 19, 19.5 é 20)
def round_school(x):
    d = 0
    if math.floor((x % 1) * 10) >= 5: d = 1
    return (int(x) + d)

# Este bloco de código pergunta ao utilizador se Educação Física conta para a média do secundário
ef_conta = input("Educação Física conta para a média do secundário no teu ano? (Sim / Não) - ")
while ef_conta not in sn:
    ef_conta = input("A resposta tem de ser sim ou não! - ")
if ef_conta in sim: ef_conta = True
if ef_conta in nao: ef_conta = False

time.sleep(1)

# Este bloco de código pergunta ao utilizador se os Exames Nacionais do 11º contam para a média do secundário
exame_conta11 = input("Os Exames Nacionais 11º Ano contam para a média do secundário no teu ano? (Sim / Não) - ")
while exame_conta11 not in sn:
    exame_conta11 = input("A resposta tem de ser sim ou não! - ")
if exame_conta11 in sim: exame_conta11 = True
if exame_conta11 in nao: exame_conta11 = False

time.sleep(1)

# Este bloco de código pergunta ao utilizador se os Exames Nacionais do 12º contam para a média do secundário
exame_conta12 = input("Os Exames Nacionais 12º Ano contam para a média do secundário no teu ano? (Sim / Não) - ")
while exame_conta12 not in sn:
    exame_conta12 = input("A resposta tem de ser sim ou não! - ")
if exame_conta12 in sim: exame_conta12 = True
if exame_conta12 in nao: exame_conta12 = False

time.sleep(1)

# Este bloco de código pergunta ao utilizador se fez exame de Filosofia em vez de uma das duas disciplinas específicas
bexame_fil = input("Fizeste Exame Nacional de Filosofia ao invés de uma das duas disciplinas específicas? (Sim / Não) - ")
while bexame_fil not in sn:
    bexame_fil = input("A resposta tem de ser sim ou não! - ")
if bexame_fil in sim: bexame_fil = True
if bexame_fil in nao: bexame_fil = False

# Se o utilizador realizou exame a Filosofia, este bloco de código pergunta qual das 2 específicas escolheu não fazer exame
examere = 0
if bexame_fil: examere = int(input("Qual exame não realizaste para trocar com o de Filosofia? (1/2 para Disciplina Específica 1/2) - "))
while examere not in [1,2]:
    examere = input("A resposta tem de ser 1 ou 2! - ")
if examere == 1: 
    bexame_esp1 = False
    bexame_esp2 = True
if examere == 0:
    bexame_esp2 = False
    bexame_esp1 = True

time.sleep(1)

print("---------------------------------------------------------------------------------------------------------------------")

time.sleep(1)

print("Então, vou-te perguntar todas as tuas notas ao longo do 10º, 11º e 12º anos ")

time.sleep(1)

# Este bloco de código pergunta ao utilizador as notas do 10º, 11º e 12º ano de Matemática
nota_mat10 = int(input("Qual foi a tua nota à disciplina trienal no final do 10º ano? - "))
nota_mat11 = int(input("Qual foi a tua nota à disciplina trienal no final do 11º ano? - "))
nota_mat12 = int(input("Qual foi a tua nota à disciplina trienal no final do 12º ano? - "))

# Este bloco de código pergunta ao utilizador, se o exame contar para a média, a nota do exame de Matemática
if exame_conta12:
    exame_mat = round_school(int(input("Qual foi a nota que obtiveste no exame da disciplina trienal? (0-20, arredondado às unidades) - ")))

time.sleep(1)

# Este bloco de código pergunta ao utilizador as notas do 10º, 11º e 12º ano de Português
nota_pt10 = int(input("Qual foi a tua nota a Português no final do 10º ano? - "))
nota_pt11 = int(input("Qual foi a tua nota a Português no final do 11º ano? - "))
nota_pt12 = int(input("Qual foi a tua nota a Português no final do 12º ano? - "))

# Este bloco de código pergunta ao utilizador, se o exame contar para a média, a nota do exame de Português
if exame_conta12:
    exame_pt = round_school(int(input("Qual foi a nota que obtiveste no exame de Português? (0-20, arredondado às unidades) - ")))

time.sleep(1)

# Este bloco de código pergunta ao utilizador, se EF contar para a média, as notas do 10º, 11º e 12º ano de Educação Física
if ef_conta:
    nota_ef10 = int(input("Qual foi a tua nota a Educação Física no final do 10º ano? "))
    nota_ef11 = int(input("Qual foi a tua nota a Educação Física no final do 11º ano? "))
    nota_ef12 = int(input("Qual foi a tua nota a Educação Física no final do 12º ano? "))

time.sleep(1)

# Este bloco de código pergunta ao utilizador as notas do 10º e 11º ano da específica 1
nota_esp10_1 = int(input("Qual foi a tua nota à disciplina específica 1 no final do 10º ano? - "))
nota_esp11_1 = int(input("Qual foi a tua nota à disciplina específica 1 no final do 11º ano? - "))

# Este bloco de código pergunta ao utilizador , tendo ele realizado exame a essa disciplina e se o exame contar para a média, a nota do exame da específica 1
if exame_conta11 and bexame_esp1:
    exame_esp1 = round_school(int(input("Qual foi a nota que obtiveste no exame da disciplina específica 1? (0-20, arredondado às unidades) - ")))

time.sleep(1)

# Este bloco de código pergunta ao utilizador as notas do 10º e 11º ano da específica 2
nota_esp10_2 = int(input("Qual foi a tua nota à disciplina específica 2 no final do 10º ano? - "))
nota_esp11_2 = int(input("Qual foi a tua nota à disciplina específica 2 no final do 11º ano? - "))

# Este bloco de código pergunta ao utilizador , tendo ele realizado exame a essa disciplina e se o exame contar para a média, a nota do exame da específica 2
if exame_conta11 and bexame_esp2:
    exame_esp2 = round_school(int(input("Qual foi a nota que obtiveste no exame da disciplina específica 2? (0-20, arredondado às unidades) - ")))

time.sleep(1)

# Este bloco de código pergunta ao utilizador as notas do 10º e 11º ano da disciplina de Lingua Estrangeira
nota_ling10 = int(input("Qual foi a tua nota à Lingua Estrangeira no final do 10º ano? - "))
nota_ling11 = int(input("Qual foi a tua nota à Lingua Estrangeira no final do 11º ano? - "))

time.sleep(1)

# Este bloco de código pergunta ao utilizador as notas do 10º e 11º ano de Filosofia
nota_fil10 = int(input("Qual foi a tua nota a Filosofia no final do 10º ano? - "))
nota_fil11 = int(input("Qual foi a tua nota a Filosofia no final do 11º ano? - "))

# Este bloco de código pergunta ao utilizador , tendo ele realizado exame a essa disciplina e se o exame contar para a média, a nota do exame de Filosofia
if bexame_fil:
    exame_fil = round_school(int(input("Qual foi a nota que obtiveste no exame de Filosofia? (0-20, arredondado às unidades) - ")))

time.sleep(1)

# Este bloco de código pergunta ao utilizador a nota do 12º ano da Opção 1
nota_op1 = int(input("Qual foi a tua nota na Opção 1 no final do 12º ano? - "))

time.sleep(1)

# Este bloco de código pergunta ao utilizador a nota do 12º ano da Opção 2
nota_op2 = int(input("Qual foi a tua nota na Opção 2 no final do 12º ano? - "))

time.sleep(1)

print("---------------------------------------------------------------------------------------------------------------------")

print("Hum... Vou-te dizer a tua média! Deixa-me só pensar um pouco...")

time.sleep(1)

# Este bloco de código calcula, se os exames do 12º ano contarem para a média, a média de Português e Matemática já com exames
if exame_conta12:
    nota_mat = round_school ( ( ( nota_mat10 + nota_mat11 + nota_mat12 ) / 3 ) * 0.7 + exame_mat * 0.3 )
    nota_pt = round_school  ( ( ( nota_pt10 + nota_pt11 + nota_pt12 ) / 3 ) * 0.7 + exame_pt * 0.3 )

# Este bloco de código calcula, se os exames do 11º ano contarem para a média, a média da específica 1, 2 e Filosofia já com exames (se eles forem feitos)
if exame_conta11:
    if bexame_esp1: nota_esp1 = round_school ( ( ( nota_esp11_1 + nota_esp10_1 ) / 2 ) * 0.7 + exame_esp1 * 0.3 )
    else: nota_esp1 = round_school ( ( ( nota_esp11_1 + nota_esp10_1 ) / 2 ) )
    if bexame_esp2: nota_esp2 = round_school ( ( ( nota_esp11_2 + nota_esp10_2 ) / 2 ) * 0.7 + exame_esp2 * 0.3 )
    else: nota_esp2 = round_school ( ( ( nota_esp11_2 + nota_esp10_2 ) / 2 ) )
    if bexame_fil: nota_fil = round_school ( ( ( nota_fil10 + nota_fil11 ) / 2 ) * 0.7 + exame_fil * 0.3 )
    else: nota_fil = round_school ( ( nota_fil10 + nota_fil11 ) / 2 )

# Este bloco de código calcula, se os exames do 12º ano não contarem para a média, a média de Português e Matemática
if not exame_conta12:
    nota_mat = round_school ( ( nota_mat10 + nota_mat11 + nota_mat12 ) / 3 )
    nota_pt = round_school ( ( nota_pt10 + nota_pt11 + nota_pt12 ) / 3 )

# Este bloco de código calcula, se os exames do 11º ano não contarem para a média, a média da específica 1, 2 e Filosofia
if not exame_conta11:
    nota_esp1 = round_school ( ( ( nota_esp11_1 + nota_esp10_1 ) / 2 ) )
    nota_esp2 = round_school ( ( ( nota_esp11_2 + nota_esp10_2 ) / 2 ) )
    nota_fil = round_school ( ( nota_fil10 + nota_fil11 ) / 2 )

# Este bloco de código calcula, se Educação Física contar para a média, a média de Educação Física
if ef_conta:
    nota_ef = round_school ( ( nota_ef10 + nota_ef11 + nota_ef12 ) / 3 )

# Esta linha de código calcula a nota da disciplina de Lingua Estrangeira
nota_ling = round_school ( ( nota_ling10 + nota_ling11 ) / 2 )

# Este bloco de código calcula, se EF contar para a média, a Média Final do secundário arredondada à 2ª casa decimal
if ef_conta:
    media = round ( ( nota_mat + nota_pt + nota_ling + nota_fil + nota_esp1 + nota_esp2 + nota_ef + nota_op1 + nota_op2 ) / 9 , 2 )

# Este bloco de código calcula, se EF não contar para a média, a Média Final do secundário arredondada à 2ª casa decimal
if not ef_conta:
    media = round ( ( nota_mat + nota_pt + nota_ling + nota_fil + nota_esp1 + nota_esp2 + nota_op1 + nota_op2 ) / 8 , 2 )

print("A tua média é " + str(media) + " !")

time.sleep(3)

print("---------------------------------------------------------------------------------------------------------------------")

input("Gostaste? Obrigado por usares este programa! Segue-me no twitter: @tugauga ")

time.sleep(60)