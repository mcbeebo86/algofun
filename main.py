from StringAlgorithms.Palindromes import Palindromes
from StringAlgorithms.LargestRectangleHistogram import LargestRectangleHistogram

def executePaliTests():
    #words = ["bat", "tab", "cat"]
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    pali = Palindromes(words)
    pali.solve()

def executeHistogramTests():
    src = "/Users/vladimirpyagay/PycharmProjects/AlgoFun/tests/test.txt"
    lrgRec = LargestRectangleHistogram(src)
    lrgRec.solve()

def main():
    #executePaliTests()
    executeHistogramTests()

if __name__ == "__main__":
    main()
