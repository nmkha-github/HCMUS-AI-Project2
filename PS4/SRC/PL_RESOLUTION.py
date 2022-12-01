from lib import negative_alpha


def PL_RESOLVE(clauseA, clauseB):

    return 1


def PL_RESOLUTION(KB, alpha):
    clauses = KB + negative_alpha(alpha)
    new = []
    while True:
        resolvents = []
        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):
                resolvents.append(PL_RESOLVE(clauses[i], clauses[j]))
        if len(resolvents) == 0:
            return True
