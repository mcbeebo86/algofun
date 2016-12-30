from StringAlgorithms.Palindromes import Palindromes
from StringAlgorithms.LargestRectangleHistogram import LargestRectangleHistogram
from StringAlgorithms.LargestRectangleMatrix import LargestRectangleMatrix
from NumberAlgorithms.TwoSum import TwoSum
from NumberAlgorithms.ThreeSum import ThreeSum

class TestSuite:

    def __init__(self):
        pass

    def executePaliTests(self):
        # words = ["bat", "tab", "cat"]
        words = ["abcd", "dcba", "lls", "s", "sssll"]
        pali = Palindromes(words)
        pali.solve()

    def executeHistogramTests(self):
        src = "/Users/vladimirpyagay/PycharmProjects/AlgoFun/tests/test.txt"
        lrgRec = LargestRectangleHistogram(src)
        lrgRec.solve()

    def executeMatrixTests(self):
        mSize = 4
        src = [[0 for x in range(mSize)] for y in range(mSize)]  # Square matrix
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

    def executeNumberTests(self):
        # srcArr = [2, 7, 11, 15]
        srcArr = [-1, 0, 1, 2, -1, -4]
        target = 0

        twos = TwoSum(srcArr, target)
        twos.solve()

        threes = ThreeSum(srcArr, target)
        threes.solve()

    def run(self):
        # self.executePaliTests()
        # self.executeHistogramTests()
        # self.executeMatrixTests()
        self.executeNumberTests()
