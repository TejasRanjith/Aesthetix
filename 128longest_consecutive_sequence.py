
def longestConsecutive(self, nums: list[int]) -> int:
    if len(nums) == 1:
        return 1
    nums.sort()
    print(nums)
    count,results=0,[0]
    for i in range(1,len(nums)):
        if (nums[i] - nums[i-1]) == 1:
            count+=1
            results.append(count+1)
        elif nums[i] == nums[i-1]:
            continue
        else:
            count=0
    return(max(results))
        
# longestConsecutive(1,[100,4,200,1,3,2])
print(longestConsecutive(1,[9,1,4,7,3,-1,0,5,8,-1,6]))
print(longestConsecutive(1,[1,0,1,2]))
print(longestConsecutive(1,[0,0]))