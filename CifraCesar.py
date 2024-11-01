class CifraCesar:
    text: str
    ctext: str
    # chave: int

    def __init__(self, text:str) -> None:
        self.text = text
        # self.chave = chave

    def cifrar(self, chave: int) -> str:
        ctext = ""
        
        if chave>26 or chave<-26:
            chave = chave%26
            
        for char in self.text:

            charValue = ord(char)
            charAscii = charValue + chave
            # print(f"char: {char} - Ascii dec: {charValue}", end=" ")

            if (charValue >= 65 and charValue <= 90) or (charValue >= 97 and charValue <= 122):
                
                if (charAscii > 90 and charValue <= 90) or (charAscii > 122 and charValue <= 122):
                    ctext += chr(charAscii-26)
                    continue
                elif (charAscii < 65 and charValue >= 65) or (charAscii < 97 and charValue >= 97):
                    ctext += chr(charAscii+26)
                    continue
                else:
                    ctext += chr(charAscii)
            else:
                ctext += char
        self.ctext = ctext
        return ctext

    def decifrar(self, chave: int) -> str | None:
        dtext = self.cifrar(-chave)
        return dtext if dtext == self.text else None #Caso o texto decifrado não seja igual o texto original, retornará nada
    
    def forcabruta(self, words_file_path='./palavras.txt') -> list | None:
        texts = self.text.split()

        with open(words_file_path, 'r', encoding='UTF-8') as file:
            palavras = file.read().split()
        
        # print(texts)
        # print(palavras)

        chaves = {}

        for i in range(len(texts)):
            palavra = texts[i]
            chave = 0

            while chave<=26:
                # chaves.update({chave: 0})

                # print(f'Chave: {chave}\n Palavra: {palavra}')
                dpalavra = CifraCesar(palavra).cifrar(-chave)
                # print(f' Decifrada: {dpalavra}')
                
                if(dpalavra in palavras):
                    # print('palavra in palavras encontrado!!!')
                    chaves.update({chave: chaves[chave]+1} if chaves.__contains__(chave) else {chave: 1})
                    break

                chave+=1
        # print('\n\nChaves: \n')
        print(chaves)
        # print(max(chaves.values()))
        c = max(chaves, key=chaves.get)
        # print(f'chave: {c}')

        return [c, self.cifrar(-c)] if c>0 else None #Retorna None caso não tenha conseguido encontrar nenhuma chave correspondente

            