class Solution:
    def __init__(self):
        self.arr = [] 
        self.count = 0 
    def heapifyUp(self, arr, ind):
        parentInd = (ind - 1)//2 
        if ind >0 and arr[ind]<arr[parentInd]:
            arr[ind],arr[parentInd]=arr[parentInd],arr[ind]
            self.heapifyUp(arr,parentInd)
        return
    def heapifyDown(self, arr, ind):
        n = len(arr)
        smallestInd = ind
        # Indices of the left and right children
        leftChildInd = 2*ind + 1
        rightChildInd = 2*ind + 2

        if leftChildInd < n and arr[leftChildInd] < arr[smallestInd]:
            smallestInd = leftChildInd
        if rightChildInd < n and arr[rightChildInd] < arr[smallestInd]:
            smallestInd = rightChildInd
        if smallestInd != ind:
            arr[smallestInd], arr[ind] = arr[ind], arr[smallestInd]
            self.heapifyDown(arr, smallestInd)
        return

    def initializeHeap(self):
        self.arr.clear()
        self.count=0 
        

    def insert(self, key):
        self.arr.append(key)
        self.heapifyUp(self.arr, self.count)
        self.count += 1
        return
        

    def changeKey(self, index, new_val):
        if self.arr[index] > new_val:
            self.arr[index] = new_val
            self.heapifyUp(self.arr, index)
        else:
            self.arr[index] = new_val
            self.heapifyDown(self.arr, index)
        return
        

    def extractMin(self):
        ele = self.arr[0] 
        self.arr[0], self.arr[self.count - 1] = self.arr[self.count - 1], self.arr[0]
        self.arr.pop()
        self.count -= 1
        if self.count > 0:
            self.heapifyDown(self.arr, 0)
        

    def isEmpty(self):
        return (self.count == 0)
        

    def getMin(self):
        return self.arr[0]
        

    def heapSize(self):
        return self.count
        