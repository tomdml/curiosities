from PIL import Image
import random

random.seed('123546')

original = Image.open('scrambled.png')

shuffled = [*range(len(original.getdata()))]
random.shuffle(shuffled)

zipped = list(zip(original.getdata(), shuffled))
newpixels = sorted(zipped, key=lambda x: x[1])
newpixels = [a for a, b in newpixels]

with open('output.png', 'wb') as fp:
    output = Image.new(original.mode, original.size)
    output.putdata(newpixels)
    output.save(fp)
