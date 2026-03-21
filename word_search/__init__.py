from word_search.functions01 import searchWord, printResult
from word_search.functions02 import searchWord02, printResult02

def main01():
    grid = [['a', 'b', 'a', 'b'],
            ['a', 'b', 'e', 'b'],
            ['e', 'b', 'e', 'b']]
    word = "abe"

    ans = searchWord(grid, word)
    printResult(ans)


def main02():
    grid = [['a', 'b', 'a', 'b'],
            ['a', 'b', 'e', 'b'],
            ['e', 'b', 'e', 'b']]
    word = "abe"

    ans = searchWord02(grid, word)

    printResult02(ans)
