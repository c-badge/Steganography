from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw()

# ask user for an image and load the pixels
input('Press enter to choose an image to format...')
pic = askopenfilename()
im = Image.open(pic)
px = im.load()

# format pixels (specifically, only the R attribute of each pixel)
for x in range(im.width):
    for y in range(im.height):
        r,g,b = px[x,y]
        if r%2 == 1:
            r = r-1
        px[x,y] = (r,g,b)

# save formatted image
path, ext = pic.split('.')
im.save(path + '_formatted.png', 'PNG')