# Pesquisa Binária - Jogo de Adivinhação

## Objetivo do Projeto

Este repositório foi criado como parte da minha jornada para fortalecer os fundamentos de programação, com foco especial em:

### Reforço da Lógica de Programação
- **Desafio atual**: Tenho enfrentado dificuldades com raciocínio algorítmico
- **Estratégia**: Prática consistente além do conteúdo teórico
- **Abordagem**: 
  - Implementação de todos os exemplos do livro "Entendendo Algoritmos"
  - Criação de variações e casos adicionais
  - Solução de problemas complementares

### Compartilhamento de Conhecimento
- **Para devs iniciantes** que:
  - Estão iniciando em algoritmos
  - Enfrentam desafios similares com lógica
  - Buscam exemplos práticos e didáticos
- **Material**:
  - Códigos comentados
  - Explicações passo a passo
  - Comparações entre abordagens

## Contexto de Estudo

**Livro base**: ["Entendendo Algoritmos"](https://github.com/KAYOKG/BibliotecaDev/blob/main/LivrosDev/Entendendo%20Algoritmos%20-%20Um%20Guia%20Ilustrado%20Para%20Programadores%20e%20Outros%20Curiosos%20-%20Autor%20(Aditya%20Y.%20Bhargava).pdf) (Aditya Bhargava)  
**Metodologia**:
1. Leitura teórica
2. Implementação prática
3. Criação de variações
4. Documentação do processo
5. Aplicação em problemas reais

## Descrição
Este projeto implementa um jogo de adivinhação que utiliza o algoritmo de pesquisa binária para encontrar um número escolhido pelo usuário entre 1 e 100. O programa demonstra a eficiência da pesquisa binária, que consegue encontrar qualquer número no intervalo em no máximo 7 tentativas.

## Como Funciona
1. O programa gera uma lista de números de 1 a 100
2. O usuário escolhe mentalmente um número nesse intervalo
3. O programa inicia a busca binária:
   - Faz um "chute" no meio do intervalo atual
   - Pergunta se o número do usuário é maior, menor ou igual ao chute
   - Ajusta o intervalo de busca com base na resposta
4. O processo se repete até que o número seja encontrado

## Exemplo de Uso
```
O número que você escolheu é maior, menor ou igual a 50? maior
O número que você escolheu é maior, menor ou igual a 75? menor
O número que você escolheu é maior, menor ou igual a 62? igual
Acertei! O número escolhido é 62.
```

## Benefícios da Pesquisa Binária
- Extremamente eficiente (encontra qualquer número em 1-100 em no máximo 7 tentativas)
- Demonstra o poder dos algoritmos de divisão e conquista
- Ilustra o conceito de complexidade logarítmica (O(log n))
