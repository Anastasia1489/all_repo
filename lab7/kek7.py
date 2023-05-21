from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageFont

sample = Image.open('овца.jpg')
sample.show()

hor = ImageOps.mirror(sample)
hor.save('овца_гор.jpg')
ver = ImageOps.flip(sample)
ver.save('овца_вер.jpg')


im1 = Image.open('1.jpg')
im2 = Image.open('2.jpg')
im3 = Image.open('3.jpg')
im4 = Image.open('4.jpg')
im5 = Image.open('5.jpg')

edg1 = im1.filter(ImageFilter.FIND_EDGES)
edg2 = im2.filter(ImageFilter.FIND_EDGES)
edg3 = im3.filter(ImageFilter.FIND_EDGES)
edg4 = im4.filter(ImageFilter.FIND_EDGES)
edg5 = im5.filter(ImageFilter.FIND_EDGES)

edg1.save('1_kek.jpg')
edg2.save('2_kek.jpg')
edg3.save('3_kek.jpg')
edg4.save('4_kek.jpg')
edg5.save('5_kek.jpg')

image = Image.open('овца.jpg')
draw = ImageDraw.Draw(image)

bl = (3, 7, 12)
font = ImageFont.truetype("kekkek.ttf", 40)
draw.text((0, 0), "KEKEKE", fill=bl, font=font)
image.show()
image.save('лул_овца.jpg')
