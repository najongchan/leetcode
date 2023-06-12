# https://leetcode.com/problems/snapshot-array/
import bisect


class SnapshotArray:

    def __init__(self, length: int):
        self.snap_data = [[[-1, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.snap_data[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        id = bisect.bisect(self.snap_data[index], [snap_id+1])
        return self.snap_data[index][id-1][1]


# Your SnapshotArray object will be instantiated and called as such:
obj = SnapshotArray(1)
obj.set(0, 4)
obj.set(0, 16)
obj.set(0, 13)
param_2 = obj.snap()
param_3 = obj.get(0, 0)
param_4 = obj.snap()
print(param_2)
print(param_3)
print(param_4)