
class LargestRectangleHistogram:

    def __init__(self, inputFile):
        self.inputFile = inputFile

    def convertStringArrayToIntArray(self, arr):
        res = []
        for i in range(len(arr)):
            res.append(int(arr[i]))

        return res

    def solveCase(self, caseArrSize, caseArr):
        if not caseArr or len(caseArr) < 1: return

        #for each element in array, go left and right comparing to min height until smaller height or edge
        caseMax = 0
        for i in range(caseArrSize):
            curMin = caseArr[i]

            #check to the left
            j = i - 1
            leftCount = 0
            while j > 0:
                if (caseArr[j] < caseArr[i]): break

                leftCount += 1
                j -= 1

            #check to the right
            j = i + 1
            rightCount = 0
            while j < caseArrSize:
                if (caseArr[j] < caseArr[i]): break

                rightCount += 1
                j += 1

            totalSize = (leftCount + rightCount + 1) * curMin
            if totalSize > caseMax: caseMax = totalSize

        print (caseMax)

    def solveCase2(self, caseArrSize, caseArr):
        stack = []
        i = 0
        max_area = 0

        while i < len(caseArr):
            if len(stack) == 0 or caseArr[stack[-1]] <= caseArr[i]:
                stack.append(i)

                # increment i ONLY WHEN PUSHING TO STACK! i == RIGHT MOST POINTER!
                i += 1
            else:
                top = stack.pop()
                prevTop = i if len(stack) == 0 else (i - stack[-1] - 1)
                top_area = caseArr[top] * prevTop
                if max_area < top_area: max_area = top_area

        while len(stack) > 0:
            top = stack.pop()
            prevTop = i if len(stack) == 0 else (i - stack[-1] - 1)
            top_area = caseArr[top] * prevTop
            if max_area < top_area: max_area = top_area

        print (max_area)

    def solve(self):
        caseArrSize = 0
        lineCounter = 0
        inCase = False
        delim = " "

        with open(self.inputFile, 'r') as f:
            for line in f:
                lineCounter += 1
                if lineCounter == 1:
                    totalCases = int(line)
                else:
                    if not inCase:
                        caseArrSize = int(line)
                        inCase = True
                    else:
                        curArr = line.split(delim)
                        self.solveCase2(caseArrSize, self.convertStringArrayToIntArray(curArr))
                        inCase = False