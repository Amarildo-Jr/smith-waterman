# Algoritmo Smith-Waterman

## Introdução

Este repositório contém a implementação em Python do algoritmo Smith-Waterman, desenvolvido como parte da disciplina de Tópicos em Bioinformática. O algoritmo é projetado para realizar alinhamento global de sequências de DNA.

## Algoritmo Smith-Waterman

### Parâmetros de Entrada

- **Sequências:** As sequências a serem alinhadas são fornecidas em um arquivo de entrada no formato de texto. Cada sequência ocupa uma linha.

- **Parâmetros:**
  - **Gap:** Pontuação aplicada para cada posição em que há um gap.
  - **Mismatch:** Penalidade para cada posição onde os caracteres das sequências não correspondem.
  - **Match:** Pontuação para cada posição onde os caracteres das sequências coincidem.

### Estrutura do Código

O código-fonte está organizado em funções principais:

1. **`build_alignment_matrix(seq1, seq2, gap, match, mismatch)`**
   - Constrói a matriz de alinhamento e a matriz de rastreamento.
   - Inicializa as pontuações com base nas pontuações fornecidas.
   - Preenche a matriz usando as regras do algoritmo Smith-Waterman.

2. **`matrix_print(matrix, matrix_name)`**
   - Gera uma representação formatada da matriz para facilitar a visualização.

3. **`backtrace(traceback_matrix, seq1, seq2)`**
   - Realiza o backtrace a partir da célula de pontuação máxima, gerando os alinhamentos das sequências.

4. **`__main__`**
   - Leitura das sequências e parâmetros do arquivo de entrada.
   - Chamada da função principal `build_alignment_matrix`.
   - Execução do backtrace e escrita dos resultados no arquivo de saída `output.txt`.

## Utilização

1. **Entrada:**
   - Crie um arquivo de entrada chamado `input.txt` com o formato especificado.
   - Insira as sequências, valores de gap, mismatch e match no padrão a seguir:
     - Na linha 1 colocar a primeira sequencia (vertical)
     - Na linha 2 colocar a segunda sequencia (horizontal)
     - Na linha 3 colocar o valor de GAP  
     - Na linha 4 colocar o valor de mismatch
     - Na linha 5 colocar o valor de match- 
  > ⚠️ É importante se atentar para entradas mal formatadas ou com espaços indesejados. Verifique se a entrada está correta antes de executar o algoritmo.
2. **Execução:**
   - Execute o arquivo `main.py`.

3. **Saída:**
   - O resultado será gravado no arquivo `output.txt`.
   - A matriz de alinhamento final, a matriz de rastreamento final e os alinhamentos das sequências serão apresentados.

## Considerações Finais

- Este é um projeto educacional e deve ser utilizado para fins acadêmicos. Caso haja dúvidas ou problemas, entre em contato com o professor da disciplina.
