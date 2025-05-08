# Cria uma lista de números de 1 a 100 usando a função range()
lista = list(range(1, 101))

# Define a função que implementa o algoritmo de busca binária para adivinhar o número
def pesquisa_binaria(lista):
    # Inicializa os índices que delimitam a área de busca
    baixo = 0               # Índice inicial da lista
    alto = len(lista) - 1   # Índice final da lista (último elemento)
    tentativas = 0

    # Mensagem inicial para o usuário
    print('Pense em um número de 1 a 100 e eu tentarei adivinhar!')

    # Loop principal da busca binária
    while baixo <= alto: # Garante que a busca continue enquanto ainda tiverem números a serem verificados
        # Calcula o índice do meio da lista atual
        meio = (baixo + alto) // 2  # Divisão inteira para pegar o índice médio
        
        # Obtém o valor do elemento no meio da lista atual (nosso "chute")
        chute = lista[meio] # Acessa o valor na posição meio da lista. O chute chute sempre será o chute: [50, 25, 12 ...]
        tentativas += 1  # Incrementa o contador a cada tentativa
        
        # Mostra o chute para o usuário
        print(f'É {chute}?')
        
        # Pede a resposta do usuário e processa:
        # - strip() remove espaços em branco no início/fim
        # - lower() converte para minúsculas
        resposta = input("Digite 'certo', 'menor' ou 'maior': ").strip().lower()

        # Verifica a resposta do usuário
        if resposta == 'certo':
            # Se acertou, mostra mensagem e encerra a função
            print(f"Acertei! O número é {chute}.")
            print(f"Foram necessárias {tentativas} tentativa(s) para acertar.")
            return
        elif resposta == 'menor':
            # Se o número do usuário é menor, ajusta o limite superior
            alto = meio - 1 # Se é menor que 50(meio), o alto agora é 49
        elif resposta == 'maior':
            # Se o número do usuário é maior, ajusta o limite inferior
            baixo = meio + 1 # Se é maior que 50(meio), o baixo agora é 51
        else:
            # Resposta inválida - pede para tentar novamente
            print("Resposta inválida! Digite 'certo', 'menor' ou 'maior'.")

    # Se saiu do loop sem encontrar, o usuário provavelmente deu respostas inconsistentes
    print("Hmm, parece que houve um erro. Você tem certeza que pensou em um número entre 1 e 100?")

# Chama a função passando a lista de 1 a 100
pesquisa_binaria(lista)