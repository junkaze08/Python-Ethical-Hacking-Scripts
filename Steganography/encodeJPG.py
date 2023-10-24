#Inserting string to a jpeg
with open ('moon.jpg', 'ab') as f:
    f.write(b"Hello World")
    