#https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids):
        keep = True
        while keep:
            for i in range(len(asteroids)):
                if asteroids[i] < 0:
                    if i > 0 and asteroids[i]*asteroids[i-1] < 0:
                        if asteroids[i-1] + asteroids[i] == 0:
                            del asteroids[i]
                            del asteroids[i - 1]
                        elif asteroids[i-1] + asteroids[i] > 0:
                            del asteroids[i]
                        else:
                            del asteroids[i-1]
                        break

                if i == len(asteroids)-1 and asteroids[i] > 0:
                    return asteroids

            if len(asteroids) <= 0:
                return asteroids
            else:
                if asteroids[0] > 0:
                    flag = 1
                else:
                    flag = -1

                for j in asteroids:
                    if j * flag < 0:
                        keep = True
                        break
                    else:
                        keep = False

        return asteroids

    def stack_asteroidCollision(self, asteroids):
        stack = []

        for element in asteroids:
            while len(stack) > 0 and stack[-1] > 0 and element < 0:
                if stack[-1] < -element:
                    stack.pop()
                    continue
                elif stack[-1] == -element:
                    stack.pop()
                break
            else:
                stack.append(element)

        return stack


# a = Solution()
# x = a.stack_asteroidCollision([8, -8])
# y = a.stack_asteroidCollision([-2, -1, 1, 2])
# z = a.stack_asteroidCollision([5,10,-5])
# print(x)
# print(y)
# print(z)