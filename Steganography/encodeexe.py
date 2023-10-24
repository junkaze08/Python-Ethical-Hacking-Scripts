with open('moon.jpg', 'ab') as f, open('procexp64.exe', 'rb') as e:
    f.write(e.read())
