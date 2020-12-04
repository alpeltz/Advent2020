import sys
nums = {}
sums = {}
for line in sys.stdin:
    line.strip()
    num = int(line)
    target = 2020-num
    if target in sums:
        print(sums[target][0]*sums[target][1]*num)
    if num not in nums:
        for n in nums.keys():
            # store intermediate sum
            sums[n + num] = [n, num]
        nums[num] = True
