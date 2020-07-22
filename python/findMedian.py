"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the 
median is the mean of the two middle value.

For example,
[2,3,4], the median is 3
[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:
void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
"""

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def addNum(self, num: int) -> None:
        if len(self.arr) == 0:
            self.arr.append(num)
            return
        low = 0
        high = len(self.arr) - 1
        
        while low <= high:
            mid = (low + high)//2
            if self.arr[mid] == num:
                self.arr.insert(mid, num)
                return
            elif self.arr[mid] < num:
                low = mid + 1
            else:
                high = mid - 1
        self.arr.insert(low, num)
        

    def findMedian(self) -> float:
        leng = len(self.arr)
        if leng == 0:
            return
        if leng%2 == 0:
            return (self.arr[int(leng/2)] + self.arr[int(leng/2)-1])/2
        else:
            return self.arr[leng//2]

obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian()) # -> 1.5
obj.addNum(3) 
print(obj.findMedian()) # -> 2