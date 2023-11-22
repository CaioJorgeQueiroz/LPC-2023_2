import random
import string

string_final = "METHINKS IT IS LIKE A WEASEL"
letras = string.ascii_uppercase + " "
string_inicial = ""
taxa_mutacao = 0.05
tentativa = 0


def primeira_string():
    global string_inicial
    for i in range(28):
        string_inicial += random.choice(letras)
    return string_inicial


primeira_string()


def copias(string_inicial):
    copias_string_inicial = []
    for i in range(50):
        copias_string_inicial.append(string_inicial)
    return copias_string_inicial


def mutacao(descendentes):
    for i in range(len(descendentes)):
        string_mutada = ""
        for caracter in descendentes[i]:
            if random.uniform(0, 1) <= taxa_mutacao:
                string_mutada += random.choice(letras)
            else:
                string_mutada += caracter
        descendentes[i] = string_mutada
    return descendentes


def pontuacao(descendentes):
    global string_final
    lista_pontuacoes = []
    for string in range(len(descendentes)):
        pontuacao = 0
        for caracter in range(len(descendentes[string])):
            if descendentes[string][caracter] == string_final[caracter]:
                pontuacao += 1
        lista_pontuacoes.append(pontuacao)
    return lista_pontuacoes


def melhor_pontuacao(lista_pontuacoes):
    melhor_pontuacao = 0
    indice = 0
    for i in range(len(lista_pontuacoes)):
        if lista_pontuacoes[i] > melhor_pontuacao:
            melhor_pontuacao = lista_pontuacoes[i]
            indice = i
    return melhor_pontuacao, indice


descendentes_mutados = mutacao(copias(string_inicial))
pontuacoes = pontuacao(descendentes_mutados)
maior_pontuacao, indice = melhor_pontuacao(pontuacoes)
print(
    f"String inicial :{string_inicial}"
)

while maior_pontuacao < 28:
    descendentes_mutados = mutacao(copias(descendentes_mutados[indice]))
    tentativa += 1
    pontuacoes = pontuacao(descendentes_mutados)
    maior_pontuacao, indice = melhor_pontuacao(pontuacoes)
    print(
        f"String {tentativa}: {descendentes_mutados[indice]}  Pontuação : {maior_pontuacao} "
    )

print(
    f"A string alvo foi alcançada após {tentativa} tentativas."
)
