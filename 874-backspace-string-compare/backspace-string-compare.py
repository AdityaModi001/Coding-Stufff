class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        string_stack1 = []
        string_stack2 = []
        for i in range(len(s)):
            if s[i] != '#':
                string_stack1.append(s[i])
            else:
                if string_stack1:
                    string_stack1.pop()
                else:
                    continue
        
        for i in range(len(t)):
            if t[i] != '#':
                string_stack2.append(t[i])
            else:
                if string_stack2:
                    string_stack2.pop()
                else:
                    continue
        
        if string_stack1 == string_stack2:
            return True
        else:
            return False
