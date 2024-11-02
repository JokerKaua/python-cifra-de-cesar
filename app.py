from CifraCesar import CifraCesar
import json

def saveJsonFile(jsonDict: dict, filePath='config.json'): 
    with open(filePath, 'w', encoding='UTF-8') as file:
        json.dump(jsonDict, file)

def saveTextFile(text: str, filePath='text.txt'):
    with open(filePath, 'w', encoding='UTF-8') as file:
        file.write(text)

while True:
    print('\nSelecione uma opção\n1. Cifrar\n2. Decifrar\n0. Sair')
    op = int(input())
    if op == 0:
        break
    elif op == 1:
        text = input('Digite o texto: ')
        chave = int(input('Digite a chave: '))
        cifra = CifraCesar(text)
        textoCifrado = cifra.cifrar(chave)
        
        print(f'Texto cifrado: {textoCifrado}\n\nSalvando configuração em "config.json"')
        saveConfig = input('Salvar para "forcabruta"? [s] / [n]')

        if saveConfig == 'n':
            config = {'modo':'decifrar', 'chave':chave}
        elif saveConfig == 's': 
            config = {'modo':'forcabruta'}

        saveJsonFile(config)
        saveTextFile(textoCifrado)

    elif op == 2:
        text = input('Digite o texto: ')
        chave = int(input('Digite a chave: '))
        cifra = CifraCesar(text)
        dtext = cifra.decifrar(chave)

        print(f'Texto decifrado: {dtext}\n\nSalvando configuração em "config.json"')       
        saveJsonFile({'modo':'cifrar', 'chave': chave})
        saveTextFile(dtext)
        
    else:
        print('\nSelecione um opção válida\n')