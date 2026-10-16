import sys 
class Solution:
    def minOperations(self, logs: list[str]) -> int:
        main_folder = []
        n  =len(logs)
        for i in range(n):
            if logs[i] == './':
                continue
            if logs[i] != '../':
                main_folder.append(1)

            else:
                if not main_folder:
                    continue 
                else:
                    main_folder.pop()
        return len(main_folder)
