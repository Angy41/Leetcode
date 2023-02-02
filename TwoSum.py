List=[1,5,5,3,2]
Target=10

def twoSum(nums,target):
    dict={}
    for i, num in enumerate(nums):
        t=target-num
        if t in dict:
            return [dict[t], i]
        dict[num]=i
    return[]

print(twoSum(List,Target))