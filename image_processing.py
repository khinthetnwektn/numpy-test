from PIL import Image
import numpy as np

imagePath = "../test/sample.png"
resultImagePath = "../test/result.png"

print("image path=>", imagePath)

img = Image.open(imagePath)
image = np.array(img)

tempimg = image.copy()

tempimg[:, :, (1, 2)] = 0

black_pixels_mask = np.all(tempimg == [255, 0, 0], axis=-1)
tempimg[black_pixels_mask] = [255, 255, 255]

pil_img = Image.fromarray(tempimg)
pil_img.save(resultImagePath)
