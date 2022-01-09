class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        met_dot = met_e = met_digit = False
        for i, c in enumerate(s) :
            if c in '+-':
                if i > 0 and s[i-1] != 'e':
                    return False
            elif c == '.':
                if met_e or met_dot:
                    return False
                met_dot = True
            elif c.lower() == 'e':
                if not met_digit or met_e:
                    return False
                met_e = True
                met_digit = False
            elif c.isdigit():
                met_digit = True
            else:
                return False
        
        return met_digit
            
                
        