def largest_adjacent_product(filename, span):
    file = open(filename)
    nums = file.read()
    largest = list_mult(nums[:span])
    index = 0
    for start in range(1, len(nums) - span):
        candidate = list_mult(nums[start:start+span])
        if candidate > largest:
            largest = candidate
            index = start
    product = nums[index]
    for char in nums[index+1:index+span]:
        product += " X " + char
    print(f"{product} = {largest}")
def list_mult(nums):
    total = 1
    for num in nums:
        total *= int(num)
    return total
largest_adjacent_product("number.txt", 13)
