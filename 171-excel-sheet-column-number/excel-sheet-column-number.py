class Solution(object):

    def titleToNumber(self, columnTitle):

        result = 0

        for ch in columnTitle:
            value = ord(ch) - 64
            result = result * 26 + value

        return result