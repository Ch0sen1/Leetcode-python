class Solution:
    def myAtoi(self, s: str) -> int:
        state = value = pos = 0
        sign = 1
    
        # state 0 = empty space, nothing to do
        # state 1 = + - case, only 
        while pos < len(s):
            char = s[pos]
            if state == 0:
                if char == ' ':
                    state = 0
                elif char in '+-':
                    state = 1
                    if char == '+':
                        sign = 1
                    else:
                        sign = -1
                elif char.isdigit():
                    state = 2
                    value = value * 10 + ord(char) - ord('0')
                else:
                    return 0
            elif state == 1:
                if char.isdigit():
                    state = 2
                    value = value * 10 +ord(char) - ord('0')
                else:
                    return 0
            elif state == 2:
                if char.isdigit():
                    value = value * 10 + ord(char) - ord('0')
                else:
                    break
            else:
                return 0
            
            pos += 1
            
        value = sign * value
        value = min(value, 2 ** 31 - 1)
        value = max(-(2 ** 31), value)
            
        return value
                    
                    
            
        