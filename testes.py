from CifraCesar import CifraCesar

#chave 4 - "Teste de texto para decifrar"
# "owy owk psj pkj" -> Retorna um dict com todos as chaves e textos

cifra = CifraCesar("owy owk psj pkj")

# print(cifra.decifrar(3))

forcabruta = cifra.forcabruta()

if type(forcabruta) == dict:
    for chave, texto in forcabruta.items():
        print(f'\nChave: {chave}\nTexto:{texto}')
else:
    print(forcabruta)