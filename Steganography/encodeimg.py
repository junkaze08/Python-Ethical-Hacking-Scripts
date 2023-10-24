#Encoding PNG file to JPG file
import PIL.Image
import io

img = PIL.Image.open('code.png')
byte_arr = io.BytesIO()
img.save(byte_arr, format='PNG')

with open('moon.jpg', 'ab') as f:
    f.write(byte_arr.getvalue())