class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            arr[0] = -1
        else:
            for i in range(len(arr)):
                curMax = -1
                # find max element from i+1 to end of array
                for j in range(i+1, len(arr)):
                    if arr[j] > curMax:
                        curMax = arr[j]
                # replace ith element with curMax 
                arr[i] = curMax
            
        return arr