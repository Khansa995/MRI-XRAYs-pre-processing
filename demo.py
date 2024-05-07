import math
print(math.ceil(1.2))
print(math.factorial(5))
import math as m
result=m.ceil(4.3)
result1=m.factorial(2)
print(result,result1)
import math
print(math.tau)
from math import *
print(math.pi)
import numpy as np
arr=np.array([1,2])
print(arr)
print(type(arr))
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
print(arr.data)
print(arr.itemsize)
print(arr.strides)
import numpy as np
arr=np.array(10)
print(arr)
print(type(arr))
import numpy as np
mylist=[[1,2,3],
        [4,5,6],
        [5,6,7]]
arr=np.array(mylist)
print(arr)
import numpy as np
mylist=[[1],[2],[3],[4]]
arr=np.array(mylist)
print(arr)
print(arr.ndim)
import numpy as np
arr=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(arr)
import numpy as np
arr=np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print('array:',arr)
print('strides',arr.strides)
import numpy as np
arr=np.empty(3)
print('empty',arr)
arr=np.ones((2,3))
print(arr)
arr=np.empty((2,3),dtype=np.int16)
print(arr)
import numpy as np
arr=np.full(7,54)
print(arr)
arr=np.full(7,21.5)
print(arr)
arr=np.full((2,3),21.5)
print(arr)
arr=np.fromstring('2.5 3.0 3.5 40.0', sep= ' ')
print(arr)
import numpy as np
import sys
list1=range(1000)
print(len(list1))
element_size=sys.getsizeof(list1)
list_size=element_size*len(list1)
print('size of each element={} and size of list1={}bytes'.format(element_size,list_size))
array1=np.arange(1000,dtype=np.uint8)
print('array1'.format(array1.itemsize,array1.nbytes))
import numpy as np
array1=np.array([1,2,3,4])
array2=np.array([5,6,7,8])
array3=array1*array2
print(array3)
import numpy as np
array1=np.array([1,2,3,4])
array2=np.array([5,6,7,8])
for i in range(0,4):
    array3[i]=array1[i] * array2[i]
print(array3)
import numpy as np
import time
size=1000000
array1=np.arange(size)
array2=np.arange(size)
initialtime=time.time()
array3=array1*array2
finaltime=time.time()
print('\ntime taken by numpy arrays is',finaltime-initialtime,'seconds')
import numpy as np
arr=np.random.randint(1,10,size=4)
print(arr)
print(arr+2)
print('subtract',arr-2)
print(arr%2)
import numpy as np
arr=np.random.rand(5)*10
print(arr)
print(np.abs(arr))
print(np.cbrt(arr))
import numpy as np
mylist=[4,5,6,7,0,2,3]
arr=np.array(mylist)
print(arr.shape)
print(arr[0])
print(arr[-7])
import numpy as np
mylist=[
    [1,2,3,4],
    [5,6,7,8],
    [9,0,12,5],
    [6,90,87,6]
]
arr=np.array(mylist)
print(arr.shape)
print(arr[3][2])
print(arr[3,2])
print(arr[3])
import numpy as np
mylist=[[[1,2,3],[4,5,6],[7,8,9]],
        [[1,2,3],[4,5,6],[7,8,9]]]
arr=np.array(mylist)
print(arr)
print(arr.shape)
print(arr.ndim)
print(arr[0])
print(arr[1][1])
import numpy as np
mylist=[1,2,3,4,5]
arr=np.array(mylist)
print(arr[:])
print(arr[3:])
print(arr[1:3])
print(arr[::-1])
print(arr)
import numpy as np
list1=[1,2,3,4,5,6,7,8,9]
arr1=np.array(list1)
print(arr1)
arr2=arr1[2:6]
print(arr2)
arr2[0]=99
print(arr2)
print(arr1)
import numpy as np
mylist=[
    [1,2,3,4],
    [5,6,7,8],
    [0,9,8,7]
]
arr=np.array(mylist)
print(arr)
print(arr.shape)
print(arr[:,:])
print(arr[2])
print(arr[2,:])
print(arr[:,1])
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,9,0]])
print(arr)
print(arr[0,2])
print(arr[2])
import numpy as np
arr=np.random.randint(1,101,10)
print(arr)
print(arr[np.array([0,2,7,8])])
print(arr[[0,2,7,8]])
import numpy as np
arr=np.random.randint(1,101,10)
print(arr)
print(arr[arr%2==0])
print(arr[arr%2==1])
import numpy as np
mylist=[4,5,6,7,0,2,3]
arr=np.array(mylist)
print(arr.shape)
import numpy as np
arr1=np.random.randint(1,50,size=5)
arr2=np.random.randint(1,10,size=5)
print(arr1)
print(arr2)
print(arr1+arr2)
import numpy as np
arr1=np.arange(24)
print(arr1)
print(arr1.shape)
arr1.shape=(6,4)
print(arr1)
print(arr1.ndim)
print(arr1.shape)

