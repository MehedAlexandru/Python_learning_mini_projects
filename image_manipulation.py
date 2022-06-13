from PIL import Image, ImageFilter


img = Image.open('./charm.jpg')
out = img.filter(ImageFilter.BLUR)
out.save("blur.png", "png")





