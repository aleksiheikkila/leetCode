class Solution:
    def numDecodings(self, s: str) -> int:
        # DP
        # Like 1/2 step "how many way to get to the end"
        if not s or s[0] == "0":
            return 0
        
        # added one extra to the beginning of the dp
        dp = [0 for _ in range(len(s) + 1)]
        dp[0:2] = [1, 1]  # dp[1] = 1 as the case of leading "0" is already handled
        
        for i in range(1, len(s)):
            # one step jump
            if 1 <= int(s[i]):
                dp[i+1] += dp[i]
            # two step jump
            if 10 <= int(s[i-1:i+1]) <= 26:
                dp[i+1] += dp[i-1]
                
        return dp[-1]
            
    
    def numDecodings_slow(self, s: str) -> int:
        rst = 0
        #idx = 0
        stack = [0]
        N = len(s)
        
        while stack:
            #print("Stack", s)
            #sstr = s.pop()
            idx = stack.pop()
            if idx >= N:
                #print("Found:", parts)
                rst += 1
                continue
            
            #print(idx)
            first = int(s[idx])
            if 1 <= first <= 9:
                stack.append(idx+1)
                
                if idx < N - 1 and int(s[idx:idx+2]) <= 26:
                    stack.append(idx+2)
                
        
        return rst