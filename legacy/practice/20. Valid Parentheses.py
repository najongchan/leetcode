class Solution:
    def isValid(self, s: str) -> bool:
        candidate = []
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        openParent = list(pairs.keys())
        print(openParent)
        s = list(s)

        for i in range(len(s)):
            if s[i] in openParent:
                candidate.append(s[i])
            else:
                last_opened = candidate.pop()
                if pairs[last_opened] != s[i]:
                    return False
        if len(candidate) > 0:
            return False
        else:
            return True