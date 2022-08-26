import json


def return_massa(name) -> str:
    with open("dir_massa/massa.json", encoding='utf-8') as meu_json:
        dados = json.load(meu_json)
    for dado in dados:
        return dado['massa'][name]