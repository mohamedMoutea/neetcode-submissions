class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False
        
        s1_dict = {}
        window_count = {}

        for char in s1:
            s1_dict[char] = s1_dict.get(char,0)+1

        for i in range(len(s1)):
            char = s2[i]
            window_count[char] = window_count.get(char,0)+1

        for i in range(len(s1),len(s2)):

            if s1_dict == window_count:
                return True
            else:
                window_count[s2[i]] = window_count.get(s2[i],0)+1
                window_count[s2[i-len(s1)]] -= 1
                if window_count[s2[i-len(s1)]] == 0:
                    del window_count[s2[i-len(s1)]]

        return s1_dict == window_count 