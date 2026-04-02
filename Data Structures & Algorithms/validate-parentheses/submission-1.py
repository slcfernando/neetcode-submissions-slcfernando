class Solution:
    def isValid(self, s: str) -> bool:
        pairing = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c in pairing:
                if not stack or stack[-1] != pairing[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return not stack