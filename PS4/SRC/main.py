import sys
import os
from lib import *
from PL_RESOLUTION import PL_RESOLUTION


def main():
    print(remove_duplicate_element([[], [], []]))
    test_case = 0
    for inputFile in os.listdir('INPUT'):
        KB, alpha = read_input('INPUT/' + inputFile)
        print("alpha: ", alpha)
        print("Negative alpha:", negative_clause(alpha))
        print("KB:", KB)

        result, output = PL_RESOLUTION(KB, alpha)

        write_output('OUTPUT/output' + str(test_case) +
                     '.txt', result, output)
        for new_clauses in output:
            print(len(new_clauses))
            for clause in new_clauses:
                if clause:
                    print(' OR '.join(clause))
                else:
                    print('{}')

        print("YES" if result else "NO")

        test_case += 1


if __name__ == '__main__':
    main()
