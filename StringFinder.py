# @Author Edward Carter

import sympy


class StringFinder:

    def start(self):
        selection = input('Please enter a String: ')
        print(self.findLargestRepeatingSubstring(selection))

    #  This method takes in a String and searches for the largest substring that would fit inside it
    #  @Ret -1 if no suitable substring can be found
    def findLargestRepeatingSubstring(self, inStr) -> str:
        stringLen = len(inStr)

        if stringLen <= 1:
            return '-1'

        elif sympy.isprime(stringLen):
            if self.isStringDivisible(inStr[0: 1], inStr):
                return inStr[0: 1]
            else:
                return '-1'

        elif stringLen % 2 == 0:  #Even length
            i = stringLen
            while i % 2 == 0:
                i = i // 2  #We only want to check first half of the string or less for repeats
                if self.isStringDivisible(inStr[0: i], inStr):
                    return inStr[0: i]
                if sympy.isprime(i):
                    if self.isStringDivisible(inStr[0: 2], inStr):
                        return inStr[0: 2]
                    if self.isStringDivisible(inStr[0: 1], inStr):
                        return inStr[0: 1]
                    return '-1'

        else:  #Non-prime odd length
            divArray = self.findDivisorsDesc(stringLen)
            for div in divArray:
                if self.isStringDivisible(inStr[0: div], inStr):
                    return inStr[0: div]

        return '-1'

    def isStringDivisible(self, inSub, inStr) -> bool:
        origSub = inSub
        while len(inSub) <= len(inStr):
            if inSub == inStr:
                return True
            inSub = inSub + origSub
        return False

    def findDivisorsDesc(self, inLen) -> []:
        i = inLen // 2
        divisorsArray = []
        while i > 0:
            if inLen % i == 0:
                divisorsArray.append(i)
            i = i - 1
        return divisorsArray
