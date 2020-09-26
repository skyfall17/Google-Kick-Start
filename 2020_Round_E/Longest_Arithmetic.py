cases = int(input())
for c in range(cases):
    n = int(input())
    nums = input().split(" ") # strings of numbers
    maximum = 2
    curr = 2
    diff = int(nums[1]) - curr
    for i in range(1, len(nums)):
        second = int(nums[i])
        first = int(nums[i - 1])
        if second - first == diff:
            curr += 1
        else:
            diff = second - first
            curr = 2
        maximum = max(maximum, curr)
    print("Case #{}: {}".format(c + 1, maximum))
