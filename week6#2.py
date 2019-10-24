# https://leetcode.com/problems/sort-colors/
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        use counting sort
        """
        color_map = {
            "red": 0,
            "white": 1,
            "blue": 2
        }

        count_list = {}
        count_list[color_map['red']] = nums.count(color_map['red'])
        count_list[color_map['white']] = nums.count(color_map['white'])
        count_list[color_map['blue']] = nums.count(color_map['blue'])

        ex_value = 0
        for key, value in count_list.items():
            for i in range(ex_value, ex_value + value):
                nums[i] = key
            ex_value += value

        return
        
        
input = [2,0,2,1,1,0]
# output = [0,0,1,1,2,2]
temp = Solution()
print(temp.sortColors(input))