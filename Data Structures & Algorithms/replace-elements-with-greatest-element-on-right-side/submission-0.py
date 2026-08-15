class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rM=-1
        for i in range(len(arr)-1, -1 ,-1):
            newM=max(rM, arr[i])
            arr[i]=rM
            rM=newM
        return arr