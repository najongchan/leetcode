# https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, S: str):
        print(S)
        S = list(S)

        partition_list = []
        pos = dict()
        count = dict()
        index = 0
        for s in S:
            if s in count:
                count[s] += 1
            else:
                count[s] = 1

            pos[s] = index
            index += 1

        max_v = 0
        key_list = []
        for key, value in pos.items():
            if max_v < value:
                max_v = value
            key_list.append(key)

            compare = 0
            for k in key_list:
                compare += count[k]

            shift = 0
            for _ in partition_list:
                shift += _

            if compare == max_v+1 - shift:
                partition_list.append(max_v+1-shift)
                max_v = 0
                key_list = []

        return partition_list


a = Solution()
x = a.partitionLabels("ababcbacadefegdehijhklij")
print(x[0])
print(x[1])