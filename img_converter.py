from PIL import Image
import os
import sys


# grab first and second arg

# first = sys.argv[1]
directory = sys.argv[1] + "/"
path_dir = './poke/'
path = os.path.join(path_dir, directory)

print(path)
#check if directory exists, if not create one

if os.path.isdir(f'{path}') is not True:
    os.mkdir(path)

# loop trough path and convert JPG to PNG
# save them to the new folder
for file in os.listdir(path_dir):
    f, e = os.path.splitext(file)
    if file.endswith(".jpg"):
        img = Image.open(f"{path_dir}{file}")
        img.save(f"{path}{f}.png", "png")














    # outfile = f + ".png"
    # try:
    #     with Image.open(file) as im:
    #         im.save(outfile)
    # except OSError:
    #     print("cannot convert", file)
