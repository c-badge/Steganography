from PIL import Image
from datetime import datetime
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
Tk().withdraw()

st_bin = ''
im = ''
px = ''

# get string from user and convert to binary. then format binary to same lengths
def format_str():
    global st_bin
    st = input('Enter string to encode in image: ')
    st_bin = ' '.join(format(ord(x), 'b') for x in st)
    bin_list = []
    for b in st_bin.split(' '):
        bin_list.append(b)
    for x in range(len(bin_list)):
        if len(bin_list[x]) == 6:
            bin_list[x] = '0' + bin_list[x]
    st_bin = ''.join(bin_list)
    get_image()

# get image from user and load the pixels
def get_image():
    global im
    global px
    print('\n!!! IMAGE SHOULD BE PROPERLY FORMATTED AND A PNG !!!\n')
    input('Press Enter to choose image...')
    im = Image.open(askopenfilename())
    px = im.load()
    encode_str()

# go pixel by pixel in image and set red according to value of current place in binary string
def encode_str():
    global st_bin
    global px
    global im

    # used to keep track of place in binary string
    count = 0

    for x in range(im.width):
        for y in range(im.height):
            if count == len(st_bin):
                save_image()
            r,g,b = px[x,y]
            if st_bin[count] == '1':
                r += 1
            px[x,y] = (r,g,b)
            count += 1
        if count == len(st_bin):
            save_image()

# formatting filename and saving image
def save_image():
    input('\nPress enter to choose directory to save image...')
    directory = askdirectory()
    dt = datetime.now()
    im.save(directory + '/Success ' + dt.strftime('%Y-%m-%d %H-%M-%S') + '.png', 'PNG')
    exit()

format_str()