from PIL import Image, ImageFilter, ImageDraw, ImageFont


input_name = input()
im = Image.open(input_name)
im_crop = im.crop((10, 700, 400, 900))
im_crop.save('1' + input_name)
