class Solution:
    def isPalindrome(self, s: str) -> bool:  
        s = [c for c in s.lower() if c.isalnum()]

        # if filtering out results in no alphanumeric chars
        if not s:
            return True

        for i in range(len(s) // 2 + 1):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True