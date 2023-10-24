#!/usr/bin/python

from PIL import Image

scrambled1 = Image.open('scrambled1.png')
scrambled2 = Image.open('scrambled2.png')
size = width, height = scrambled1.size

new = Image.new('RGB', size)

scrambled1 = scrambled1.load()
scrambled2 = scrambled2.load()
data = new.load()

for x in range(width):
    for y in range(height):
        
        one = scrambled1[x,y]
        two = scrambled2[x,y]
        
        new_color = (one[0] ^ two[0],
                     one[1] ^ two[1],
                     one[2] ^ two[2])
        
        data[x,y] = new_color
        
new.save('result.jpg')
new.show()

#Comparing two images using XOR pixel values of 2 images to create a new image that combines visual information from 2 image source