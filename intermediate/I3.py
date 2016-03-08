"""
For two segments of integer [l1, r1] and [l2, r2]. How many pair (x, y) which l1 <= x <= r1 and l2 <= y <= r2 where x * y divisible by p.
Input
The first line is integer p (1 <= p <= 10^9)
Second line includes l1, r1 separated by a space (1 <= l1 <= r1 <= 10^9).
Third line includes l2, r2 separated by a space (1 <= l2 <= r2 <= 10^9).
"""

p = int(raw_input("input p:"))
seg1 = raw_input("input l1 r1:")
seg2 = raw_input("input l2 r2:")

l1 = int(seg1.split(" ")[0])
r1 = int(seg1.split(" ")[1])
l2 = int(seg2.split(" ")[0])
r2 = int(seg2.split(" ")[1])

count = 0
tlist = list()
for x in range(l1, r1+1):
    for y in range(l2, r2+1):
        if x*y%p == 0:
            count += 1
            tlist.append((x,y))

print count
print tlist