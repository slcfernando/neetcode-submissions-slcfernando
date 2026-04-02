class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # rule out different length strings
        if len(s) != len(t):
            return False
    
        # use arrays to store counts of each character
        s_counts = [0] * 26
        t_counts = [0] * 26

        for s_char, t_char in zip(s, t):
            s_counts[ord(s_char) - ord('a')] += 1
            t_counts[ord(t_char) - ord('a')] += 1
        
        # compare the counts
        for i in range(26):
            if s_counts[i] != t_counts[i]:
                return False
        return True