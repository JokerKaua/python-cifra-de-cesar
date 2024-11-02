from CifraCesar import CifraCesar

#chave 4 - "Teste de texto para decifrar" - "Xiwxi hi xibxs teve higmjvev"
cifra = CifraCesar("Xiwxi hi xibxs teve higmjvev")

forcabruta = cifra.forcabruta()

print(forcabruta[0])
print(forcabruta[1])