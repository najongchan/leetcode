# https://leetcode.com/problems/perfect-squares/
class Solution(object):
    # bfs
    def bfsNumSquares(self, n: int) -> int:
        if n < 2:
            return n

        square_list = [i*i for i in range(1, int(n**0.5) + 1)]

        count = 0
        check_list = {n}

        while check_list:
            count += 1
            temp = set()
            for j in check_list:
                for k in square_list:
                    if j == k:
                        return count
                    elif j < k:
                        break
                    else:
                        temp.add(j-k)
            check_list = temp
        return count

    # dp
    def dpNumSquares(self, n: int) -> int:
        dp = [_ for _ in range(n+1)]
        squares_list = [_*_ for _ in range(1, int(n**0.5) + 1)]

        for i in range(1, n+1):
            # print(i)
            for square in squares_list:
                # print(square)
                # print(dp)
                if i - square < 0:
                    break
                else:
                    dp[i] = min(dp[i], dp[i-square]+1)
        return dp[n]


# a = Solution()
# print(a.bfsNumSquares(12))
# print(a.dpNumSquares(12))