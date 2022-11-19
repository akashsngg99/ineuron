def maxi(nums):
    maxnum=-1
    for i in range(1,len(nums)):
        if(nums[i-1]>nums[i]): maxnum=nums[i-1]
        else : maxnum=nums[i]
    print(maxnum)

nums=[4,1,9,3]
maxi(nums)

