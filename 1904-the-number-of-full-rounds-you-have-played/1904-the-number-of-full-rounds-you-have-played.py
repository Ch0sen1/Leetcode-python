class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        # 1 hr have 4 round
        hs = int(loginTime[:2])
        ms = int(loginTime[-2:])
        
        ts = 60 * hs + ms
        
        hf = int(logoutTime[:2])
        mf = int(logoutTime[-2:])
        
        tf = 60 * hf + mf
        
        return max(0, tf//15 - (ts+14)//15 + (ts>=tf)*96)
        
        
        
        