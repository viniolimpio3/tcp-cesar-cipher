from random import randint
from Primos import Primos

class DiffieHellman: 

    def __init__(self, n, g):
        self.n = n
        self.g = g

    def implement(self):
        """
            Implementa o algoritmo Diffie-Hellman para troca de chaves
            Retorna: (n, g, private_key, public_key)
        """

        # Chave privada aleatória
        self.x = randint(1, self.n-1)

        print("X escolhido:", self.x)

        # Chave pública = g^r mod n
        r = pow(self.g, self.x, self.n)
        print("R calculado:", r)

        return r

    def compute_shared_key(self, other_x):
        """
        Computa a chave compartilhada
        shared_key = other_x^self.x mod self.n
        """
        print("Other_x recebido:", other_x)
        shared_key = pow(other_x, self.x, self.n)
        print("Chave compartilhada calculada:", shared_key)
        return shared_key