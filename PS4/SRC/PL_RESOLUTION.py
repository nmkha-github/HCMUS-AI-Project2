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

    # Trường hợp ko có literal đối ngẫu hoặc có hơn 2 literal đối ngẫu trả về câu đúng
    if literal_pairs_count != 1:
        return [True]

    # Hợp giải 2 clause
    combined_clause = [literal for literal in clauseA if literal != literal_pair[0]
                       ] + [literal for literal in clauseB if literal != literal_pair[1]]

    # Sắp xếp theo thứ tự chữ cái (A < -A)
    combined_clause.sort(key=lambda x: ord(
        x[0]) if len(x) == 1 else ord(x[1]) + 0.5)

    # Lọc các literal giống nhau
    remove_duplicate_element_in_list(combined_clause)

    return combined_clause


def PL_RESOLUTION(KB, alpha):
    output = []

    clauses = KB + [negative_clause(alpha)]
    # Chứa các clauses mới được phát sinh
    new = []

    while True:
        resolvents = []

        for i in range(len(clauses)):
            for j in range(len(clauses)):
                new_clause = PL_RESOLVE(clauses[i], clauses[j])
                if new_clause not in clauses:
                    resolvents.append(new_clause)

        # Lọc ra các clause khác true
        resolvents = [
            clause for clause in resolvents if clause != [True]]
        # Lọc các clause giống nhau
        remove_duplicate_element_in_list(resolvents)

        # print("Loop")
        # print("clauses: ", clauses)
        # print(filter_clauses)
        output.append(resolvents)

        # Nếu chứa clause rỗng thì dừng thuật toán
        if [] in resolvents:
            return True, output

        # Nếu không phát sinh các clauses mới thì dừng thuật toán
        if len(resolvents) == 0:
            return False, output

        new = new + resolvents
        clauses = clauses + resolvents
