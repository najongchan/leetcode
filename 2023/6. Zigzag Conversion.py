class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        zigzag = [['' for _ in range(len(s))] for y in range(numRows)]

        zigzag[0][0] = s[0]
        row, col, pos, vector = 0, 0, 1, 1

        while pos < len(s):
            row += vector
            if vector < 0:
                col += 1
            zigzag[row][col] = s[pos]

            if row + vector >= numRows or row + vector < 0:
                vector *= -1

            pos += 1

        answer = ''
        for zig in zigzag:
            answer += ''.join(zig)
        return answer


x = Solution()
print(x.convert("PAYPALISHIRING", 3))  # PAHNAPLSIIGYIR
print(x.convert("PAYPALISHIRING", 4))  # PINALSIGYAHRPI
print(x.convert("AB", 1))  # AB
