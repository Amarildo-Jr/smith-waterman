def build_alignment_matrix(seq1, seq2, gap, match, mismatch):
    len_seq1 = len(seq1)
    len_seq2 = len(seq2)

    # Initialize matrices for alignment and traceback directions
    alignment_matrix = [[0 for _ in range(len_seq2 + 1)] for _ in range(len_seq1 + 1)]
    traceback_matrix = [['' for _ in range(len_seq2 + 1)] for _ in range(len_seq1 + 1)]

    for i in range(1, len_seq1 + 1):
        alignment_matrix[i][0] = i * gap
        traceback_matrix[i][0] = 'up'

    for j in range(1, len_seq2 + 1):
        alignment_matrix[0][j] = j * gap
        traceback_matrix[0][j] = 'right'

    print(matrix_print(alignment_matrix, "Matriz de alinhamento preenchida com os valores iniciais"))
    print(matrix_print(traceback_matrix, "Matriz de rastreamento"))

    for i in range(1, len_seq1 + 1):
        for j in range(1, len_seq2 + 1):
            diagonal = alignment_matrix[i - 1][j - 1] + (match if seq1[i - 1] == seq2[j - 1] else mismatch)
            vertical = alignment_matrix[i - 1][j] + gap
            horizontal = alignment_matrix[i][j - 1] + gap

            # Determine the direction of the maximum value
            if diagonal >= vertical and diagonal >= horizontal:
                alignment_matrix[i][j] = diagonal
                traceback_matrix[i][j] = 'diagonal'
            elif vertical >= horizontal:
                alignment_matrix[i][j] = vertical
                traceback_matrix[i][j] = 'up'
            else:
                alignment_matrix[i][j] = horizontal
                traceback_matrix[i][j] = 'right'
        
    print(matrix_print(alignment_matrix, "Matriz de alinhamento preenchida com os valores finais"))
    print(matrix_print(traceback_matrix, "Matriz de rastreamento final"))

    return alignment_matrix, traceback_matrix

def matrix_print(matrix, matrix_name: str):
    print("=====================================================================================================")
    print(f"{matrix_name.upper()}:")
    matrix_str = ""
    for i in range(len(matrix) - 1, -1, -1):
        matrix_str += str(matrix[i]) + "\n"
    return matrix_str

def backtrace(traceback_matrix, seq1, seq2):
    align_seq1 = ""
    align_seq2 = ""
    i, j = len(seq1), len(seq2)

    while i > 0 or j > 0:
        if i > 0 and j > 0 and traceback_matrix[i][j] == 'diagonal':
            align_seq1 = seq1[i - 1] + align_seq1
            align_seq2 = seq2[j - 1] + align_seq2
            i -= 1
            j -= 1
        elif i > 0 and traceback_matrix[i][j] == 'up':
            align_seq1 = seq1[i - 1] + align_seq1
            align_seq2 = "-" + align_seq2
            i -= 1
        else:
            align_seq1 = "-" + align_seq1
            align_seq2 = seq2[j - 1] + align_seq2
            j -= 1

    return align_seq1, align_seq2

if __name__ == "__main__":
    output_file = "output.txt"

    with open(output_file, "w") as file:
        file.write("Alignment Matrix:\n")

    with open("input.txt", "r") as file:
        seq1 = file.readline().strip()
        seq2 = file.readline().strip()
        gap_penalty = int(file.readline().strip())
        mismatch_score = int(file.readline().strip())
        match_score = int(file.readline().strip())

    alignment_matrix, traceback_matrix = build_alignment_matrix(seq1, seq2, gap_penalty, match_score, mismatch_score)

    result = backtrace(traceback_matrix, seq1, seq2)

    with open(output_file, "a") as file:
        file.write("\nAligned Sequences:\n")
        file.write(result[0] + "\n")
        file.write(result[1] + "\n")

        # Calculating alignment score, match, mismatch, and gap counts
        alignment_score = alignment_matrix[len(seq1)][len(seq2)]
        match_count = sum(1 for a, b in zip(result[0], result[1]) if a == b)
        mismatch_count = sum(1 for a, b in zip(result[0], result[1]) if a != b)
        gap_count = result[0].count('-') + result[1].count('-')

        # Printing additional information
        file.write("\n------------------------------------------------------------------\n")
        file.write(f"Alignment score = {alignment_score} | Match = {match_count} | Mismatch = {mismatch_count} | Gap = {gap_count}\n")
        file.write(f"Values used: Gap = {gap_penalty}, Match = {match_score}, Mismatch = {mismatch_score}\n")
        file.write("------------------------------------------------------------------\n")
        file.write(result[0] + "\n")
        file.write(result[1] + "\n")
