class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # 2- Apply Euclid's Algorithm
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # 1- Check String Patterns
        if str1 + str2 != str2 + str1:
            return ""

        # 3- Extract the GCD String
        gcd_length = gcd(len(str1), len(str2))
        return str1[:gcd_length]
