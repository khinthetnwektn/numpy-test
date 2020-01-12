from PIL import Image
import numpy as np

imagePath = "../test/sample.png"
resultImagePath = "../test/result.png"

img = Image.open(imagePath)
image = np.array(img)

redpix = np.all(image == [255, 0, 0], axis=-1)
greenpix = np.all(image == [0, 255, 0], axis=-1)
bluepix = np.all(image == [0, 0, 255], axis=-1)

print("red   : {} pixels".format(np.sum(redpix)))
print("green  : {} pixels".format(np.sum(greenpix)))
print("blue   : {} pixels".format(np.sum(bluepix)))
