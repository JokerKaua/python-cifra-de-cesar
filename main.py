from CifraCesar import CifraCesar
import json

if __name__ == "__main__":
    #Pegando dados do config.json
    with open('config.json', 'r') as file:
        configs = json.load(file)
    #Pegando dados do text.txt    
    with open('text.txt', 'r', encoding='UTF-8') as file:
        texts = file.read()

    with open('palavras.txt', 'r', encoding='UTF-8') as file:
        palavras = file.read().split()

    cifra = CifraCesar(texts)
    chave = configs['chave'] if configs.__contains__('chave') else 0

    if configs['modo'] == 'cifrar':
        print(f'Cifrando o texto "{cifra.text}" com a chave {chave}\nTexto cifrado: {cifra.cifrar(chave)}\n')
    elif configs['modo'] == 'decifrar':
        print(f'Decifrando o texto "{cifra.text}" com a chave {chave}\nTexto decifrado: {cifra.decifrar(chave)}\n')
    elif configs['modo'] == 'forcabruta':
        print(f'Método de força bruta: \nDecifrando o texto: \n{cifra.text}\n')
        decifrado = cifra.forcabruta()
        if decifrado != None:
            print(f'Encontrado cifra com a chave {decifrado[0]}\nTexto decifrado:\n{decifrado[1]}')
        else:
            print('Nenhuma chave para o texto foi encontrada.')
