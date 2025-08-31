# Binary Files -> can store anything including music, image data
# collection of ones and zeros
# PIL -> pillow library works well with image files
# needs to install first -> pip install pillow

import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save("costumes.gif", save_all = True, append_images = [images[1]], duration = 200, loop = 100)

# on CLI -> python costumes.py costume1.gif costume2.gif
# then code costumes.gif
# make sure to save gif files in the same folder where costumes.py is stored 
# and do that in file manager