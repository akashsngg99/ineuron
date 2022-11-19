def maxi(nums):
    mult=1
    for i in range(0,len(nums)):
        mult=mult*nums[i]
    print(mult)

nums=[4,1,9,3]
maxi(nums)
