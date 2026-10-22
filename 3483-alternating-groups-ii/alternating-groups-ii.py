class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # col[i] == 0 --> the tile i is red 
        # else: 
            # we have a tile that is blue

        # n = len(colors)
        # i = 0 
        # count = 0
        # while i < n:
        #     group = []
            
        #     for j in range(k):
        #         circular_index = (i + j) % n
        #         group.append(colors[circular_index])
        #     curr_count = 0
        #     for m in range(1,len(group)):
        #         if group[m] != group[m-1]:
        #             curr_count +=1 
        #         else:
        #             break

        #     if curr_count == k-1 :
        #         count += 1
        #     i +=1

        # return count

        n = len(colors)
        count = 0 
        iter_strik = 1 
        for i in range(1, n+k-1):
            if colors[i % n] != colors[(i - 1) % n]:
                iter_strik += 1
            else:
                iter_strik = 1 
            if iter_strik >= k:
                count += 1
                    
        return count
        