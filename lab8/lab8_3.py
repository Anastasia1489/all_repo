from PIL import Image, ImageFilter, ImageDraw, ImageFont


input_name = input()
inp = input()
im = Image.open(input_name)
im_crop = im.crop((10, 700, 400, 900))
im_crop.save('1' + input_name)


font = ImageFont.truetype('nice.ttf', 40)
dr = ImageDraw.Draw(im)
dr.text(
        (0, 0),
        inp + ', поздравляем!',
        font=font,
        fill=('#1C0606'))

im.save('res.png')
