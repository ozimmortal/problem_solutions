class SumSegmentTree:

    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
    
    def build(self, idx , start , end):
        
        if start == end:
            self.tree[idx] = self.nums[start]
            return
        lidx , ridx = 2 * idx + 1 , 2 * idx + 2
        mid = (start + end) // 2
        self.build(lidx , start , mid)
        self.build(ridx , mid + 1 , end)
        self.tree[idx] = self.tree[lidx] + self.tree[ridx]

    def query(self , idx , l , r, start , end):

        if end < l or start > r:
            return 0
        if l <=start and end <= r:
            return self.tree[idx]
        
        mid = (start + end) // 2
        lidx , ridx = 2 * idx + 1 , 2 * idx + 2
        left = self.query(lidx , l , r, start , mid)
        right = self.query(ridx , l , r, mid + 1 , end)
        return left + right

    def update(self, idx, node, val, start, end):
        if start == end:
            self.nums[idx] = val
            self.tree[node] = val
            return

        mid = (start + end) // 2
        lidx, ridx = 2 * node + 1, 2 * node + 2

        if idx <= mid:
            self.update(idx, lidx, val, start, mid)
        else:
            self.update(idx, ridx, val, mid + 1, end)

        self.tree[node] = self.tree[lidx] + self.tree[ridx]
class NumArray:

    def __init__(self, nums: List[int]):
        self.store = SumSegmentTree(nums)
        self.n = len(nums)

        self.store.build(0 , 0 , self.n - 1)
    def update(self, index: int, val: int) -> None:
        self.store.update(index, 0 , val , 0 , self.n - 1)

    def sumRange(self, left: int, right: int) -> int:
        return self.store.query(0 , left , right , 0 , self.n - 1)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)