class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_counts = {}
        t_counts = {}

        for s_char, t_char in zip(s, t):
            s_counts[s_char] = s_counts.get(s_char, 0) + 1
            t_counts[t_char] = t_counts.get(t_char, 0) + 1
        
        for s_char, s_count in s_counts.items():
            if t_counts.get(s_char, 0) != s_count:
                return False
        
        return True