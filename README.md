# Comunicação TCP com Troca de Chaves Diffie-Hellman e Cifra de César

Este projeto demonstra uma implementação simples de comunicação cliente-servidor TCP com recursos de segurança adicionais:
- Protocolo TCP para transmissão confiável de dados
- Algoritmo Diffie-Hellman para troca segura de chaves
- Cifra de César para criptografia de mensagens

## Requisitos

- Python 3.x
- Biblioteca Socket (embutida no Python)

## Como Executar

### 1. Iniciar o Servidor
Primeiro, execute o servidor TCP em um terminal:
```bash
python Simple_tcpServer.py
```
O servidor começará a escutar na porta 1300.

### 2. Iniciar o Cliente
Em outro terminal, execute o cliente TCP:
```bash
python Simple_tcpClient.py
```

Observação: Por padrão, o cliente tenta se conectar ao IP "10.1.70.16". Se você estiver executando cliente e servidor na mesma máquina, você precisará modificar `serverName` em `Simple_tcpClient.py` para "localhost" ou "127.0.0.1".

## Como Funciona

1. Quando a conexão é estabelecida, o cliente e o servidor realizam uma troca de chaves Diffie-Hellman:
   - Eles usam um número primo compartilhado (n = 100000007) e uma base (g = 5)
   - Ambos os lados geram suas chaves públicas e privadas
   - Eles trocam chaves públicas e calculam uma chave secreta compartilhada

2. Após a troca de chaves:
   - O cliente recebe uma frase em minúsculas como entrada
   - A mensagem é criptografada usando a Cifra de César antes da transmissão
   - O servidor descriptografa a mensagem, converte para maiúsculas
   - O servidor criptografa a mensagem em maiúsculas e envia de volta
   - O cliente descriptografa e exibe a mensagem recebida

## Recursos de Segurança

### Troca de Chaves Diffie-Hellman
- Permite que ambas as partes estabeleçam uma chave secreta compartilhada em um canal inseguro
- Implementado em `DiffieHellman.py`
- Usa um número primo grande (100000007) para maior segurança

### Cifra de César
- Cifra de substituição simples que desloca letras por um número fixo de posições
- Implementada em `cesar_cipher.py`
- Usada para criptografar/descriptografar todas as mensagens transmitidas entre cliente e servidor

## Descrição dos Arquivos

- `Simple_tcpServer.py`: Implementação do servidor TCP
- `Simple_tcpClient.py`: Implementação do cliente TCP
- `DiffieHellman.py`: Implementação do algoritmo de troca de chaves Diffie-Hellman
- `cesar_cipher.py`: Implementação da criptografia Cifra de César
- `Primos.py`: Módulo auxiliar para operações com números primos
