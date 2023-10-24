with open('moon.jpg', 'rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))

    f.seek(offset + 2)

    with open('hidden.zip', 'wb') as z:
        z.write(f.read())