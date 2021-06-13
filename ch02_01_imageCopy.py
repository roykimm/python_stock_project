BUF_SIZE = 1024

with open('src.png', 'rb') as sf, open('dst.png','wb') as df:
    while True:
        data = sf.read(BUF_SIZE)
        if not data:
            break
        df.write(data)