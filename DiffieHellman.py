from random import randint
class DiffieHellman: 
    def diffie_hellman():
        """
            Implementa o algoritmo Diffie-Hellman para troca de chaves
            Retorna: (n, g, private_key, public_key)
        """
        
        # Parâmetros públicos (devem ser os mesmos para cliente e servidor)
        n = 23  # número primo
        g = 5   # base primitiva módulo n

        # Chave privada aleatória
        private_key = randint(1, n-1)

        # Chave pública = g^private_key mod n
        public_key = pow(g, private_key, n)
        
        return n, g, private_key, public_key

    def compute_shared_key(other_public_key, my_private_key, n):
        """
        Computa a chave compartilhada
        shared_key = other_public_key^my_private_key mod n
        """
        return pow(other_public_key, my_private_key, n)