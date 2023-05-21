from PIL import Image


kek = {}

im1 = Image.open('9may.jpg')
im2 = Image.open('8march.jpg')

kek['8 марта'] = im2
kek['9 мая'] = im1

kek[input()].show()
