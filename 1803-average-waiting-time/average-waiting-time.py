class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)

        Sum = 0 
        finish_time_1st_cus = customers[0][0] + customers[0][1] # 3
        # finish_time_chef = finish_time_1st_cus  # finish_time_chef = 3
        res = [finish_time_1st_cus]   
        # return res
        for i in range(1,len(customers)):
            arrival_time = customers[i][0]
            prep_time = customers[i][1]
            # return prep_time
            wating_time = prep_time
            finish_time_1st_cus = max(finish_time_1st_cus,arrival_time)
            finish_time_1st_cus = finish_time_1st_cus + wating_time
            res.append(finish_time_1st_cus)
        # return res
        j = 0
        for i in customers:
            Sum = Sum + (res[j] - customers[j][0])
            j += 1
        
        return Sum/len(res)

        # [7.00000,11.00000,14.00000,15.00000]
# 
            # finish_time_1st_cus = finish_time_1st_cus # 3
            # waittime_cus = finish_time_1st_cus - arrival_time #waittime_cus = 2
            # Sum += waittime_cus


