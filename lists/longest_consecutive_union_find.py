class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1
            return x

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return

        if self.size[px] < self.size[py]:
            px, py = py, px

        self.parent[py] = px
        self.size[px] += self.size[py]

def longest_consecutive_union_find(nums):
    """Find longest consecutive sequence using union-find"""
    if not nums:
        return 0

    uf = UnionFind()
    num_set = set(nums)

    # Initialize all numbers
    for num in nums:
        uf.find(num)

    # Union consecutive numbers
    for num in nums:
        if num + 1 in num_set:
            uf.union(num, num + 1)

    # Find maximum size
    return max(uf.size.values())

# Example
numbers = [100, 4, 200, 1, 3, 2]
result = longest_consecutive_union_find(numbers)
print(result)  # 4
