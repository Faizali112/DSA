class Solution:
    def toLowerCase(self, s: str) -> str:
        output = []
        for c in s:
            if c.isupper():
                output.append(chr(ord(c)+32))
            else:
                output.append(c)
        return "".join(output)
        