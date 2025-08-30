class CesarCipher:
    def __init__(self, fator=3):
        self.fator = fator

    def cript(self, texto: str):
        cripted = ""
        for i in texto:
            cripted += chr(ord(i) - self.fator)

        return cripted

    def decript(self, texto: str) -> str:
        decripted = ""
        print(texto)
        for i in texto:
            decripted += chr(ord(i) + self.fator)
        return decripted