def smith_waterman(seq1, seq2, match=3, mismatch=-1, gap=-2):
 """
 Calcula o alinhamento de Smith-Waterman entre duas sequências.

 Parâmetros:
 seq1 (str): Primeira sequência.
 seq2 (str): Segunda sequência.
 match (int): Ponto para uma correspondência.
 mismatch (int): Ponto para um desajuste.
 gap (int): Ponto para um gap.

 Retorna:
 score (int): A pontuação do alinhamento.
 score_matrix (list): A matriz de pontuação.
 """
 # Inicializa a matriz de pontuação
 score_matrix = [[0 for _ in range(len(seq2) + 1)] for _ in range(len(seq1) + 1)]

 # Preenche a matriz de pontuação
 for i in range(1, len(seq1) + 1):
     for j in range(1, len(seq2) + 1):
         if seq1[i - 1] == seq2[j - 1]:
             score = match
         else:
             score = mismatch

         score_matrix[i][j] = max(
             0,
             score_matrix[i - 1][j - 1] + score,
             score_matrix[i - 1][j] + gap,
             score_matrix[i][j - 1] + gap,
         )

 # Realiza o backtracking
 alignment1 = ""
 alignment2 = ""
 i = len(seq1)
 j = len(seq2)
 while i > 0 and j > 0:
     score_diag = score_matrix[i - 1][j - 1]
     score_up = score_matrix[i - 1][j]
     score_left = score_matrix[i][j - 1]

     if score_diag >= score_up and score_diag >= score_left:
         alignment1 += seq1[i - 1]
         alignment2 += seq2[j - 1]
         i -= 1
         j -= 1
     elif score_up >= score_left:
         alignment1 += seq1[i - 1]
         alignment2 += "-"
         i -= 1
     else:
         alignment1 += "-"
         alignment2 += seq2[j - 1]
         j -= 1

 # Inverte as sequências de alinhamento
 alignment1 = alignment1[::-1]
 alignment2 = alignment2[::-1]

 return alignment1, alignment2, score_matrix[len(seq1)][len(seq2)], score_matrix

# Leitura do arquivo de entrada
with open('input.txt', 'r') as file:
 seq1 = file.readline().strip()
 seq2 = file.readline().strip()
 gap = int(file.readline().strip())
 mismatch = int(file.readline().strip())
 match = int(file.readline().strip())

# Executa o algoritmo Smith-Waterman
alignment1, alignment2, score, score_matrix = smith_waterman(seq1, seq2, match, mismatch, gap)

# Adiciona as fitas como legenda
fitas = ['U', 'T', 'C', 'G']
score_matrix[0] = ['X'] + fitas
for i in range(1, len(score_matrix)):
   score_matrix[i][0] = fitas[i-1]

# Imprime a matriz de pontuação
print("** valores de score **")
print("=================================================================================")
for row in score_matrix:
  print(" ".join(["{:4}".format(item) for item in row]))
print("=================================================================================")

# Imprime o alinhamento e a pontuação
print("------------------------------------------------------------------")
print("Alinhamento ** score =", score, "** Match =", match, "| mismatch =", mismatch, "| Gap =", gap)
print(alignment1)
print(alignment2)
