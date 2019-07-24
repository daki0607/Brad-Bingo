from PIL import Image, ImageDraw, ImageFont
import random
from datetime import datetime
import textwrap

random.seed(datetime.now())

buffer = 40 # The buffer solution between the edges of things
thickness = 12
titleHeight = 300
color = (127, 127, 127, 255) # Made it gray so that is uses less ink
titleText = " Brad Bingo"

"""
IMPORTANT
Make sure there's a file named "phrases.txt" in the same folder!
The phrases.txt file should contain comma seperated list items like so:
Giggles,"coo",Goes to bathroom,Late to class,Banter with Daddy Dan,etc
"""

def createBoard():
    ###############################################################################
    # Board Preparation
    ###############################################################################

    # Create a new canvas to do stuff on
    im = Image.new("RGBA", (1075, 1400), (255, 255, 255, 255))

    # Tell PIL that you're drawing on the 'im' canvas
    d = ImageDraw.Draw(im)

    # borders
    d.line([(buffer, buffer), (buffer, im.height-buffer)], color, thickness)
    d.line([(buffer, im.height-buffer), (im.width-buffer, im.height-buffer)], color, thickness)
    d.line([(im.width-buffer, im.height-buffer), (im.width-buffer, buffer)], color, thickness)
    d.line([(im.width-buffer, buffer), (buffer, buffer)], color, thickness)

    # gridlines
    d.line([(buffer, titleHeight), (im.width-buffer, titleHeight)], color, thickness)
    for i in range(1, 4):
        yoffset = titleHeight + ((im.height - titleHeight - buffer) / 4) * i
        d.line([(buffer, yoffset), (im.width-buffer, yoffset)], color, thickness)

    for j in range(1, 4):
        xoffset = buffer + ((im.width - buffer - buffer) / 4) * j
        d.line([(xoffset, titleHeight), (xoffset, im.height-buffer)], color, thickness)

    ###############################################################################
    # Phrase selection
    ###############################################################################

    # Get phrases from the file
    phrases = open("phrases.txt").readline().split(",")
    random.shuffle(phrases)
    chosen = random.sample(phrases, 16)
    chosen[random.randint(0, 15)] = 'Free' # Randomly choose a free space

    # Format the text to fit in the boxes
    for i in range(16):
        chosen[i] = '\n'.join(textwrap.wrap(chosen[i], 10))

    ###############################################################################
    # Populating the boxes
    ###############################################################################

    # Title font
    font = ImageFont.truetype("Arial Bold.ttf", 150)

    # Title
    d.text((2*buffer, 2*buffer), titleText, (150, 150, 150, 255), font)

    # Box font
    font = ImageFont.truetype("Ayuthaya.ttf", 31)

    # Boxes
    for i in range(16):
        xcor = i % 4
        ycor = int(i / 4)

        textx = buffer + ((im.width - buffer - buffer) / 4) * xcor + buffer * 0.8
        texty = titleHeight + ((im.height - titleHeight - buffer) / 4) * ycor + buffer / 2
        
        d.multiline_text((textx, texty), chosen[i], (140, 140, 140, 255), font, None, 0, "center")

    return im


# Create a large canvas to print
collage = Image.new("RGBA", (2150, 2800), (255, 255, 255, 255))
# Create 4 images to put onto said canvas (4 bingo boards per sheet)
im0 = createBoard()
im1 = createBoard()
im2 = createBoard()
im3 = createBoard()

collage.paste(im0, (0, 0))
collage.paste(im1, (int(collage.width / 2), 0))
collage.paste(im2, (0, int(collage.height / 2)))
collage.paste(im3, (int(collage.width / 2), int(collage.height / 2)))

collage.save(str(random.randint(0, 100000)), "PNG")




