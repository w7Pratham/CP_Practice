class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for i in alpha:
            if i not in sentence:
                return False
        return True
