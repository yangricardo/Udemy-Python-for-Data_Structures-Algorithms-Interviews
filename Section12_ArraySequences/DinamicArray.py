import sys
import ctypes


def make_array(new_cap):  # returns a new array with new_cap capacity
    return (new_cap * ctypes.py_object)()


class DinamicArray(object):
    """
    Dinamyc Array Class
    """

    def __init__(self):
        self.length = 0  # Count number of actual elements, setting 0 by default
        self.capacity = 1  # Default capacity
        self.innerArray = make_array(self.capacity)

    def __len__(self):  # Return number of elements sorted in array
        return self.length

    def __getitem__(self, k):  # return de item at k index or an indexError
        if not 0 <= k < self.length:
            return IndexError('K is out of bounds!')
        return self.innerArray[k]

    def _resize(self, new_cap):
        auxArray = make_array(new_cap)
        for k in range(self.length):
            auxArray[k] = self.innerArray[k]

        self.innerArray = auxArray
        self.capacity = new_cap

    def append(self, ele):
        if self.length == self.capacity:  # double capacity if is full
            self._resize(2 * self.capacity)

        self.innerArray[self.length] = ele
        self.length += 1
        print("Length: {0:30}; Size in Bytes: {1:4d} ".format(self.__len__(), sys.getsizeof(self.innerArray)))


# Instantiate the new array
arr = DinamicArray()
print('Size of the array:' + str(len(arr)))
arr.append(1)
arr.append(2)
arr.append(arr[0] + arr[1])
print(arr[0])
print(arr[1])
print(arr[2])
print('New size of the array:' + str(len(arr)))

# set n
n = 10
# empty list 'data'
data = []

for i in range(n):
    # number of elements
    a = len(data)
    # actual size in bytes
    b = sys.getsizeof(data)
    print("Length: {0:30}; Size in Bytes: {1:4d} ".format(a, b))
    data.append(n)
