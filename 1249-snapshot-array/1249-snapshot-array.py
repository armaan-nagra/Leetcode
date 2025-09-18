class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.data = []
        for x in range(length):
            self.data.append([(0,0)])

    def set(self, index: int, val: int) -> None:
        if self.data[index][-1][0] == self.snap_id:
            self.data[index][-1] = (self.snap_id, val)
        else:
            self.data[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
        
    def get(self, index: int, snap_id: int) -> int:
        arr = self.data[index]

        #find snap_id (first index of each tuple) in the array elements with binary search
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = (l+r) // 2
            if arr[mid][0] < snap_id:
                l = mid + 1
            elif arr[mid][0] > snap_id:
                r = mid - 1
            else:
                return arr[mid][1]
        return arr[r][1]
        
        

        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)