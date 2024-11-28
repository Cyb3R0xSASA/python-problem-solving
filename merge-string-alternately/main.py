class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word1_len = len(word1)
        word2_len = len(word2)

        if word1_len == word2_len:
            result = [char for pair in zip(word1, word2) for char in pair]
        elif word1_len < word2_len:
            result = [char for pair in zip(word1, word2) for char in pair]
            result.append(word2[word1_len:word2_len])
        else:
            result = [char for pair in zip(word1, word2) for char in pair]
            result.append(word1[word2_len : word1_len])
        return ''.join(result)
