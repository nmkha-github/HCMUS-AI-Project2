import sys
import os
from lib import *


def main():
    for inputFile in os.listdir('INPUT'):
        KB, alpha = read_input('INPUT/' + inputFile)
        print(alpha)
        print(negative_alpha(alpha))
        print(KB)


if __name__ == '__main__':
    main()
