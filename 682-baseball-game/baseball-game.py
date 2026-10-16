import sys 
class Solution:
    def calPoints(self, operations: list[str]) -> int:
        score = []
        n =  len(operations)
        # operations = ["5","2","C","D","+"]
        for i in range(n):
            if (operations[i] != "+") and (operations[i] != 'C') and (operations[i] != 'D'):
                score.append(int(operations[i]))
                print(score)
            else:
                if operations[i] == '+':
                    score.append(score[-1] + score[-2])
                elif operations[i] == 'D':
                    score.append(2*score[-1])
                else:
                    score.pop()
        # print(score)
        return sum(score)
            