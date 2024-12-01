from sys import argv

left: list[int]
right: list[int]
left, right = [], []

try:
    file = argv[1]
except:
    file = "input.txt"

with open(file, "r") as f:
    while line := f.readline():
        item1, item2 = map(int, line.strip().split())

        left.append(item1)
        right.append(item2)

# PART 1
# sort both lists
left.sort()
right.sort()

ans = sum(abs(l - r) for l, r in zip(left, right))

print(ans)

# PART 2

ans: int = 0
for item in left:
    ans += right.count(item) * item

print(ans)
