import time
class Primos:
    @staticmethod
    def is_primo_fast(n):
        # Registrar o tempo de início
        start_time = time.time()
        primo = False
        i = 2
        while i < n:
            R = n % i
            if R == 0:
                print("{} não é primo!".format(n))
                primo = False
                break
            i += 1
        else:
            primo = True
            print("{} é primo!".format(n))

        # Registrar o tempo de término
        end_time = time.time()
        # Calcular o tempo de execução
        execution_time = end_time - start_time
        print(f"[PRIMO FAST] Tempo de execução: {execution_time:.6f} segundos")
        return primo

    @staticmethod
    def is_primo_slow(n):
        start_time = time.time()
        # Registrar o tempo de início
        start_time = time.time() 

        cont = 0
        
        i = 2

        while i < n:
            R = n % i
            if R == 0:
                cont += 1
            i += 1
        
        primo = (cont == 0)

        # Registrar o tempo de término
        end_time = time.time()
        # Calcular o tempo de execução
        execution_time = end_time - start_time
        print(f"[PRIMO SLOW] Tempo de execução: {execution_time:.6f} segundos")
        return primo
