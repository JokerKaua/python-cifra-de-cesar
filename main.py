"""
    Kauã Felipe Martins - 02/11/2024
"""

from CifraCesar import CifraCesar
import json

def saveJsonFile(jsonDict: dict, filePath='config.json'): 
    with open(filePath, 'w', encoding='UTF-8') as file:
        json.dump(jsonDict, file)
    return

def saveTextFile(text: str, filePath='text.txt'):
    with open(filePath, 'w', encoding='UTF-8') as file:
        file.write(text)
    return

def openTextFile(filePath: str) -> str:
    with open(filePath, 'r', encoding='UTF-8') as file:
       return file.read()
    
def openJsonFile(filePath: str) -> dict:
    with open(filePath, 'r', encoding='UTF-8') as file:
        return json.load(file)

if __name__ == "__main__":

    print("\x1b[2J\x1b[1;1H", end="") #Código de escape para limpar a tela

    while True:
        op = input(f'Selecione uma opção\n1. Cifrar e decifrar manualmente (salvando text.txt e cconfig.json)\n2. Ir pelos arquivos de text.txt e config.json\n0. Sair\n')
        if op.isnumeric(): #Caso a opção for um numero, converter para int
            op = int(op)
        else: # Padrão = -1 para toda opção inválida
            op = -1
        
        if op == 0:
            break
        if op == 1: # Cifrar e decifrar manualmente
            while True:
                print("\x1b[2J\x1b[1;1H", end="") #Código de escape para limpar a tela
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

                    if saveConfig.lower() == 's':
                        config = {'modo':'forcabruta'}
                    else: #Se o input for qualquer coisa diferente de 's', será salvo o modo e a chave como padrão. 
                        config = {'modo':'decifrar', 'chave':chave}
                        
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
        elif op == 2: # Cifrar e decifrar de acordo com os arquivos
            print("\x1b[2J\x1b[1;1H", end="") #Código de escape para limpar a tela

            configs = openJsonFile('config.json')
            texts = openTextFile('text.txt')
            palavras = openTextFile('palavras.txt').split()

            cifra = CifraCesar(texts)

            if configs['modo'] == 'cifrar':
                chave = configs['chave']
                print(f'Cifrando o texto: \n{cifra.text}\n\nChave {chave}\nTexto cifrado: \n{cifra.cifrar(chave)}\n')

            elif configs['modo'] == 'decifrar':
                chave = configs['chave']
                print(f'Decifrando o texto abaixo com a chave {chave}\n\n{cifra.text}\n\nTexto decifrado: {cifra.decifrar(chave)}\n')

            elif configs['modo'] == 'forcabruta':
                print(f'Método de força bruta: \nDecifrando o texto: \n{cifra.text}\n')
                decifrado = cifra.forcabruta()
                if type(decifrado) == list:
                    print(f'Encontrado cifra com a chave {decifrado[0]}\nTexto decifrado:\n{decifrado[1]}\n')
                elif type(decifrado) == dict:
                    print('Mais de uma chave encontrada para o texto.')
                    for chave, texto in decifrado.items():
                        print(f'\nChave: {chave}\nTexto:{texto}')
                else:
                    print('Nenhuma chave para o texto foi encontrada.\n')
        else: # -1
            print('\x1b[2J\x1b[1;1HDigite uma opção válida!\n')
