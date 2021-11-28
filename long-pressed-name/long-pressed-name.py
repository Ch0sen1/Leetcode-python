class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif typed[j] != typed[j-1] or j == 0:
                return False
        return i == len(name)
                
        