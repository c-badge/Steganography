from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw()

str_bin = []

input('Press Enter to choose image...')
im = Image.open(askopenfilename())
px = im.load()

def convert_bin_list():
    global str_bin
    print(len(str_bin))
    hidden_str = ''
    for b in str_bin:
        char_int = int(b, 2)
        hidden_str += chr(char_int)
    print(hidden_str)
    exit()


def get_bin():
    global str_bin
    global px
    global im
    let_bin = ''
    for x in range(im.width):
        for y in range(im.height):
            r,g,b = px[x,y]
            if r%2 == 0:
                let_bin += '0'
            else:
                let_bin += '1'
            if len(let_bin) == 7:
                if let_bin == '0000000':
                    convert_bin_list()
                str_bin.append(let_bin)
                let_bin = ''

get_bin()