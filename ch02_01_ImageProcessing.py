import requests
from PIL import Image

url = 'http://bit.ly/2JnsHnT'

r = requests.get(url, stream=True).raw

img = Image.open(r)
img.show()
img.save('src.png')

