import argparse


def levenstein(str_1, str_2):
    n, m = len(str_1), len(str_2)
    if n > m:
        str_1, str_2 = str_2, str_1
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str_1[j - 1] != str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]


parser = argparse.ArgumentParser(description="Antiplagiarism script")

parser.add_argument("-i", dest="input_file", required=True)
parser.add_argument("-o", dest="output_file", required=True)

args = parser.parse_args()

input_file = open(args.input_file, "r")
output_file = open(args.output_file, "w")

while True:
    line = input_file.readline()

    if not line:
        break

    files = line.split()

    first_file = open(files[0])
    second_file = open(files[1])

    first_f = str(first_file)
    second_f = str(second_file)

    first_file.close()
    second_file.close()

    first_f.replace("\n", "")
    second_f.replace("\n", "")
    
    similarity_score = levenstein(first_f, second_f) / len(second_f)

    output_file.write(str(similarity_score) + "\n")

input_file.close()
output_file.close()

print("All Done!")







