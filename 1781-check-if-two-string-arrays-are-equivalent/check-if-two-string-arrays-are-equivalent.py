class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        res1 = ""
        res2 = ""

        for i in range(len(word1)):
            res1 += word1[i]
    
        for i in range(len(word2)):
            res2 += word2[i]
        

        if res1 == res2:
            return True 

        else:
            return False