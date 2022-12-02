def read_clause(f):
    clause = f.readline()
    while clause[0] == " ":
        clause = clause[1:]
    while clause[len(clause)-1] == " " or clause[len(clause)-1] == '\n':
        clause = clause[:-1]
    while clause.find('  ') > -1:
        clause.replace("  ", " ")

    clause = clause.split(' OR ')

    if clause[len(clause) - 1][len(clause[len(clause) - 1]) - 1] == '\n':
        clause[len(clause) - 1] = clause[len(clause) - 1][:-1]
    return clause


def read_input(inputFile):
    f = open(inputFile, "r")
    alpha = read_clause(f)
    KB = []
    for _ in range(int(f.readline())):
        KB.append(read_clause(f))
    f.close()

    return KB, alpha


def negative_clause(alpha):
    negative_alpha = []
    for literal in alpha:
        if len(literal) == 1:
            negative_alpha.append(['-' + literal])
        else:
            negative_alpha.append([literal[1:]])

    return negative_alpha


def remove_duplicate_element_in_list(list: list):
    i = 0
    j = 0

    while i < len(list):
        j = i + 1
        while j < len(list):
            if list[i] == list[j]:
                list.pop(j)
                j -= 1
            j += 1
        i += 1

    return list


def write_output(outputFile, result, output):
    f = open(outputFile, "w")
    for new_clauses in output:
        f.write(str(len(new_clauses)) + "\n")
        for clause in new_clauses:
            if clause:
                f.write(' OR '.join(clause) + "\n")
            else:
                f.write('{}' + "\n")

    f.write("YES" if result else "NO")
    f.close()
