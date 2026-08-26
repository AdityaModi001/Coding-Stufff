class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        number_of_boats = 0 
        n = len(people)
        left = 0 
        right = len(people) -1 
        # if n % 2 == 0:
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1

            right -= 1
            number_of_boats += 1
                
        return number_of_boats

            # else:
            #     if people[i] <= limit:
            #         number_of_boats += 1
        # else:

            




        # i = 0 
        # while i < n-1: 
        #     if i >= n:
        #         break 
        #     if people[i] + people[i+1] <= limit:
        #         number_of_boats += 1
                
        #     else:
        #         if people[i] <= limit:
        #             number_of_boats += 1
        #     i +=1
         
        # return number_of_boats