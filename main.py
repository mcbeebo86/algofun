from StringAlgorithms.Palindromes import Palindromes
from StringAlgorithms.LargestRectangleHistogram import LargestRectangleHistogram
from StringAlgorithms.LargestRectangleMatrix import LargestRectangleMatrix
from NumberAlgorithms.TwoSum import TwoSum

def executePaliTests():
    #words = ["bat", "tab", "cat"]
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    pali = Palindromes(words)
    pali.solve()

def executeHistogramTests():
    src = "/Users/vladimirpyagay/PycharmProjects/AlgoFun/tests/test.txt"
    lrgRec = LargestRectangleHistogram(src)
    lrgRec.solve()

def executeMatrixTests():
    mSize = 4
    src = [[0 for x in range(mSize)] for y in range(mSize)] # Square matrix
    src[0][1] = 1
    src[0][2] = 1
    src[1][0] = 1
    src[1][1] = 1
    src[1][2] = 1
    src[1][3] = 1
    src[2][0] = 1
    src[2][1] = 1
    src[2][2] = 1
    src[2][3] = 1
    src[3][0] = 1
    src[3][1] = 1

    lrgMatrix = LargestRectangleMatrix(src)
    lrgMatrix.solve()

def executeNumberTests():
    srcArr = [2, 7, 11, 15]
    target = 18
    ts = TwoSum(srcArr, target)
    ts.solve()

def main():
    # executePaliTests()
    # executeHistogramTests()
    # executeMatrixTests()
    executeNumberTests()

if __name__ == "__main__":
    main()
