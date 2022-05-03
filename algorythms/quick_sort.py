class QuickSort:
    """Main class"""

    def __init__(self, array, l, h):
        self.sortedlist = self.quick_sort(array, l, h)

    @staticmethod
    def partition(arr, l, h):
        """Make parts from list"""
        i = (l - 1)
        x = arr[h]

        for j in range(l, h):
            if arr[j] <= x:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[h] = arr[h], arr[i + 1]
        return i + 1

    @staticmethod
    def quick_sort(arr, l, h):
        """Main function"""
        size = h - l + 1
        stack = [0] * size

        top = -1

        top = top + 1
        stack[top] = l
        top = top + 1
        stack[top] = h

        while top >= 0:
            h = stack[top]
            top = top - 1
            l = stack[top]
            top = top - 1

            p = QuickSort.partition(arr, l, h)

            if p - 1 > l:
                top = top + 1
                stack[top] = l
                top = top + 1
                stack[top] = p - 1

            if p + 1 < h:
                top = top + 1
                stack[top] = p + 1
                top = top + 1
                stack[top] = h
