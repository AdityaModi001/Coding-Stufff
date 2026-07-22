class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        n = len(arr)
        res =[]
        for i in range(n):
            if arr[i] not in arr[i+1:n] and arr[i] not in arr[0:i]:
                res.append(arr[i])
        # return res
            else:
                continue 
        
        if k <= len(res):
            return res[k-1]
        
        return ""
