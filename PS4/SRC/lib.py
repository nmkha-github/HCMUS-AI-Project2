def read_clause(f):
    clause = f.readline().split(' OR ')
    if clause[len(clause) - 1][len(clause[len(clause) - 1]) - 1] == '\n':
        clause[len(clause) - 1] = clause[len(clause) - 1][:-1]
    return clause


def read_input(inputFile):
    f = open(inputFile, "r")
    alpha = read_clause(f)
    KB = []
    for _ in range(int(f.readline())):
        KB.append(read_clause(f))

    return KB, alpha


def negative_alpha(alpha):
    negative_alpha = []
    for literal in alpha:
        if len(literal) == 1:
            negative_alpha.append('-' + literal)
        else:
            negative_alpha.append(literal[1:])

    return negative_alpha


def write_output(outputFile):
    f = open(outputFile, "w")
