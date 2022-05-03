"""Module contains binary search algorythm"""

class BinarySearch(object):
    """Main class"""

    def __init__(self,array:list):
        self.array=sorted(array)

    def search_method(self,value:int):
        """Search function"""
        start = 0
        end = len(self.array)
        while start <= end:
            middle = (start + end) // 2
            if value == self.array[middle]:
                return middle
            if value < self.array[middle]:
                end = middle - 1
            else:
                start = middle + 1

