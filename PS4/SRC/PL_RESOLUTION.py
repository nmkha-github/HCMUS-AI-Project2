from lib import negative_clause, remove_duplicate_element_in_list


def PL_RESOLVE(clauseA, clauseB):
    # Số lượng cặp literal đối ngẫu
    literal_pairs_count = 0
    # Cặp literal đối ngẫu trường hợp 2 câu có duy nhất 1 literal đối ngẫu
    literal_pair = []

    for literalA in clauseA:
        for literalB in clauseB:
            if ('-' + literalA == literalB) or (literalA == '-' + literalB):
                literal_pair = [literalA, literalB]
                literal_pairs_count += 1

    # Trường hợp ko có literal đối ngẫu hoặc có hơn 2 literal trả về câu đúng
    if literal_pairs_count != 1:
        return [True]

    # Hợp giải 2 clause
    combined_clause = [literal for literal in clauseA if literal != literal_pair[0]
                       ] + [literal for literal in clauseB if literal != literal_pair[1]]

    combined_clause.sort(key=lambda x: ord(
        x[0]) if len(x) == 1 else ord(x[1]) + 0.5)
    # Lọc các literal giống nhau
    remove_duplicate_element_in_list(combined_clause)

    return combined_clause


def PL_RESOLUTION(KB, alpha):
    clauses = KB + [negative_clause(alpha)]

    new = []
    output = []
    while True:
        resolvents = []

        for i in range(len(clauses)):
            for j in range(len(clauses)):
                new_clause = PL_RESOLVE(clauses[i], clauses[j])
                if new_clause not in clauses:
                    resolvents.append(new_clause)

        # Lọc ra các clause khác true
        filter_clauses = [
            clause for clause in resolvents if clause != [True]]
        # Lọc các clause giống nhau
        remove_duplicate_element_in_list(filter_clauses)

        # print("Loop")
        # print("clauses: ", clauses)
        # print(filter_clauses)
        output.append(filter_clauses)

        if [] in resolvents:
            return True, output

        new = new + filter_clauses

        if len(filter_clauses) == 0:
            return False, output

        clauses = clauses + filter_clauses
