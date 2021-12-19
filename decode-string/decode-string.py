class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_string = ""
        cur_num = 0
        for c in s:
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            elif c.isalpha():
                cur_string += c
            elif c == "[":
                stack.append(cur_string)
                stack.append(cur_num)
                cur_string = ""
                cur_num = 0
            elif c == "]":
                num = stack.pop()
                prev_string = stack.pop()
                cur_string = prev_string + num * cur_string
        return cur_string
            
                
                
        