class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(1,len(numbers)):
            l,r=0,len(numbers)-1
            while l<r:
                currsum=numbers[l]+numbers[r]
                if currsum>target:
                    r-=1
                elif currsum<target:
                    l+=1
                else:
                    return [l+1,r+1]
            return []