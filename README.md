# Steganography
### Simple steganography scripts written in Python. Should **NOT** be used to conceal sensitive information!

Scripts have not been tested for what happens when the length of the binary representation of a string exceeds the number of pixels in the chosen image. Scripts were tested on an image of size 640x480, meaning the maximum number of characters that can be encoded in an image of that size is 43,885, including spaces and punctuation. Using an image with a larger size will allow for longer messages to be encoded.

**format_pic.py** - Formats an image by changing the R value for each pixel to be an even integer. Currently only using the R value, which may limit the length of the message that can be encoded. Using the G and B values are in progress.

**encode.py** - Takes a string from the user, converts it to binary, then encodes it in an image by changing the R value to even or odd for each pixel in relation to each bit of the binary form of the string.

**decode.py** - Reads R value for each pixel and creates a binary number based on whether each R value is even or odd. The binary number is then converted to a string.
