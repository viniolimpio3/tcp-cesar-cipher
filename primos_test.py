import threading
import time
from Primos import Primos

def test_fast(n):
    """Função para testar o algoritmo rápido"""
    print(f"Thread Fast: Iniciando teste rápido para {n}")
    start_time = time.time()
    result = Primos.is_primo_fast(n)
    end_time = time.time()
    print(f"Thread Fast: Resultado = {result}, Tempo = {end_time - start_time:.4f}s")

def test_slow(n):
    """Função para testar o algoritmo lento"""
    print(f"Thread Slow: Iniciando teste lento para {n}")
    start_time = time.time()
    result = Primos.is_primo_slow(n)
    end_time = time.time()
    print(f"Thread Slow: Resultado = {result}, Tempo = {end_time - start_time:.4f}s")

# N Primo
n = 100000007

print(f"Testando primalidade de {n} com 2 threads...")
print("-" * 50)

# Criar as threads
thread_fast = threading.Thread(target=test_fast, args=(n,))
thread_slow = threading.Thread(target=test_slow, args=(n,))

# Iniciar as threads
start_total = time.time()
thread_fast.start()
thread_slow.start()

# Aguardar ambas terminarem
thread_fast.join()
thread_slow.join()

end_total = time.time()
print("-" * 50)
print(f"Tempo total (paralelo): {end_total - start_total:.4f}s")