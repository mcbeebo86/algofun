
class Palindromes:

    def __init__(self, testList):
        self.words = testList

    def arePalindromes(self, str1, str2):
        str3 = str1 + str2
        if (str3 == str3[::-1]):
            return True
        return False

    def solve(self):
        #All combinations of words
        #Sub proc for palindrome check
        listSize = len(self.words)
        tracker = []
        for i in range(listSize):
            for j in range(listSize):
                if i != j:
                    if self.arePalindromes(self.words[i], self.words[j]):
                        hash = str(i) + str(j)
                        if hash not in tracker:
                            tracker.append(hash)
                            print("Are palindromes: " + str(i) + " : " + str(j))

                    if self.arePalindromes(self.words[j], self.words[i]):
                        hash = str(j) + str(i)
                        if hash not in tracker:
                            tracker.append(hash)
                            print("Are palindromes: " + str(j) + " : " + str(i))
