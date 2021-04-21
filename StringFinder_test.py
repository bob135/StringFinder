# @Author Edward Carter

from StringFinder import StringFinder


def verifyEvenLengthStrings():
    testForSubstring('', '-1')
    testForSubstring('abcabc', 'abc')
    testForSubstring('abab', 'ab')
    testForSubstring('abababab', 'abab')
    testForSubstring('abcabcabcabc', 'abcabc')
    testForSubstring('aa', 'a')
    testForSubstring('aaaa', 'aa')
    testForSubstring('aaaaaa', 'aaa')
    testForSubstring('abcxabcd', '-1')
    testForSubstring('ababax', '-1')
    testForSubstring('ax', '-1')
    testForSubstring('abcabcabcabx', '-1')


def verifyOddLengthStrings():
    testForSubstring('abcabcabc', 'abc')
    testForSubstring('abcddabcddabcdd', 'abcdd')
    testForSubstring('ccccccccccccc', 'c')
    testForSubstring('ccccccccccccccccccccc', 'ccccccc')
    testForSubstring('aaa', 'a')
    testForSubstring('abcdefghi', '-1')
    testForSubstring('a', '-1')
    testForSubstring('abc', '-1')
    testForSubstring('abcab', '-1')
    testForSubstring('aaaaaab', '-1')
    testForSubstring('abcabcabx', '-1')


def testForSubstring(inStr, inSub):
    stringFinder = StringFinder();
    print('')
    print('In String: ' + inStr)
    print('Expected Result: ' + inSub)
    if stringFinder.findLargestRepeatingSubstring(inStr) == inSub:
        print('Test Passed')
    else:
        print('Test Failed')


if __name__ == '__main__':
    verifyEvenLengthStrings()
    verifyOddLengthStrings()
