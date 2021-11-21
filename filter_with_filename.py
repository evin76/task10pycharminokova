from PIL import Image
import numpy as np

img = Image.open("img2.jpg")
result_img = "res.jpg"
arr = np.array(img)
height = len(arr)
width = len(arr[1])
size = 10
gradation = 6
step = int(255 / gradation)

import doctest


def return_average(i, j, arr, size):
    """

    :type arr: object
    """
    color_sum = np.sum((arr[i: i + size, j: j + size]) / 3)
    average = int(color_sum // (size * size))
    """
    >>> return_average(0, 0, arr, 10)
    18
    """
    return average


doctest.testmod()


class Grey:
    def __init__(self, step, height, width, size, arr):
        self.step = step
        self.height = height
        self.width = width
        self.size = size
        self.arr = arr

    def getGrey(self):
        for i in range(0, self.height, self.size):
            for j in range(0, self.width, self.size):
                average = return_average(i, j, arr, size)
                self.arr[i: i + self.size, j: j + self.size] = int(average // self.step) * self.step
        return self.arr


newPicture = Grey(step, height, width, size, arr)
res = Image.fromarray(newPicture.getGrey())
res.save(result_img)
