class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_string = ""
        cur_num = 0
        
        for i in range(len(s)):
            c = s[i]
            
            if c.isdigit():
                cur_num = cur_num * 10 + (ord(c) - ord('0'))
            
            elif c.isalpha():
                cur_string += c
            
            elif c == '[':
                stack.append(cur_string)
                stack.append(cur_num)
                cur_string = ""
                cur_num = 0
            
            elif c == ']':
                prev_num = stack.pop()
                prev_string = stack.pop()
                cur_string = prev_string + (cur_string * prev_num)
            
            
        return cur_string
                
                
                
        