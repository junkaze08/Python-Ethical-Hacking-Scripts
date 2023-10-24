#Decoding and exporting PNG file from JPG file
import PIL.Image
import io

with open('moon.jpg', 'rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))
    
    f.seek(offset + 2)
    
    retrieved_img = PIL.Image.open(io.BytesIO(f.read()))
    retrieved_img.save("retrieved_image.png")