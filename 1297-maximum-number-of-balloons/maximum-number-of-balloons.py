class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        target = "balloon"

        targetFreq = {}
        textFreq = {}

        # Frequency of target
        for ch in target:
            targetFreq[ch] = targetFreq.get(ch, 0) + 1

        # Frequency of text
        for ch in text:
            textFreq[ch] = textFreq.get(ch, 0) + 1

        res = float('inf')

        for key in targetFreq:
            res = min(res, textFreq.get(key, 0) // targetFreq[key])

        return res