import json

def return_locator(name) -> []:
    lista = []
    with open("locators/locator.json", encoding='utf-8') as meu_json:
        dados = json.load(meu_json)
    for dado in dados:
       lista.append(dado[name]['by'])
       lista.append(dado[name]['value'])
    return lista
