class CifraCesar:
    text: str
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
        return ctext

    def decifrar(self, chave: int) -> str | None:
        # dtext = self.cifrar(-chave)
        # return dtext if dtext == self.text else None #Caso o texto decifrado não seja igual o texto original, retornará nada
        return self.cifrar(-chave)
    
    def forcabruta(self, words_file_path='./palavras.txt') -> list | None | dict:
        with open(words_file_path, 'r', encoding='UTF-8') as file:
            palavras = file.read().split()
        
        chaves = {}

        for palavra in self.text.split():
            chave=0
            while chave<27:
                dtext = CifraCesar(palavra).cifrar(-chave)
                if dtext in palavras and len(dtext) > 2: # Testa apenas as palavras com mais de duas letras
                    # chaves.update({chave: (chaves[chave]+1 if chaves.__contains__(chave) else 1)})
                    chaves[chave] = chaves.get(chave, 0) + 1
                    break
                chave+=1

        c = 0
        if chaves:
            s = set()
            for k in chaves.values(): 
               s.add(k)
            if len(s) == 1 and len(chaves) > 1: #Retorna todas as chaves encontradas e os textos
                r = {}
                for i in chaves.keys():
                    r.update({i: self.cifrar(-i)})
                return r
            else:
                c = max(chaves, key=chaves.get) # Caso possua algo em chaves


        return [c, self.cifrar(-c)] if c>0 else None #Retorna None caso não tenha conseguido encontrar nenhuma chave correspondente

