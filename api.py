import json
import sys

import requests


URL_ALL = "https://restcountries.com/v3.1/all"
URL_NAME = "https://restcountries.com/v2/name"

def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
    except:
        print("Erro ao realizar a requisição em https://restcountries.com/v3.1/all")

def parsing(texto_resposta):
    try:
        return json.loads(texto_resposta)
    except:
        print("Erro ao fazer parsing do Json")


def contagem_paises():
    resposta = requisicao("{}".format(URL_ALL))
    if resposta:
        lista_de_paises = parsing(resposta)
        return len(lista_de_paises)


def listar_paises():
    resposta = requisicao("{}".format(URL_ALL))
    if resposta:
        lista_de_paises = parsing(resposta)
        for pais in lista_de_paises:
            print(pais['name']['common'])

def mostrar_populacao(nome_pais):
    resposta = requisicao("{}/{}".format (URL_NAME,nome_pais))
    if resposta:
        nome_do_pais = parsing(resposta)
        if nome_do_pais:
            for pais in nome_do_pais:
                print("{}: {}".format(pais['name'], pais['population']))
        else:
            print("Pais não encontrado")

def mostrar_moedas(nome_pais):
    resposta = requisicao("{}/{}".format(URL_NAME,nome_pais))
    if resposta:
        nome_do_pais = parsing(resposta)
        if nome_pais:
            for pais in nome_do_pais:
                print("Moedas do", pais['name'])
                moedas = pais['currencies']
                for moeda in moedas:
                    print("{} - {}".format(moeda['code'],moeda['name']))


def ler_nome_pais():
    try:
        argumento2 = sys.argv[2]
        return argumento2
    except:
        print("É preciso passar o nome do país")

if __name__ == "__main__":
    if len(sys.argv) == 1:

        print("""  Bem vindo ao sistema de países
        Uso: python3 Api.py <ação> <nome do país>
        
        
        Ações disponíveis:
        contagem, listagem, moeda, populacao     
        """)
    else:
        argumento1 = sys.argv[1]
        
        if argumento1 == "contagem":
            contagem = contagem_paises()
            print("O número de países é: {}".format(contagem))

        elif  argumento1 == "listagem":
            listar_paises()

        elif argumento1 == "moeda":
            pais = ler_nome_pais()
            if pais:
                mostrar_moedas(pais)

        elif argumento1 == "populacao":
            pais = ler_nome_pais()
            if pais:
                mostrar_populacao(pais)
        
        else:
            print("Argumento inválido")
            exit(0)
            
