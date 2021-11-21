from PIL import Image
import numpy as np


def find_brightness(i, j, pixels, m_h, m_w):
    count = np.sum(pixels[i: i + m_h, j: j + m_w]) / 3
    count = count // (m_h * m_w)
    return count


def make_mosaic(pixels, mosaic_height, mosaic_width, grad):
    step_grad = 255 // (grad - 1)
    height = len(pixels)
    width = len(pixels[1])
    i = 0
    while i < height:
        j = 0
        while j < width:
            brightness = find_brightness(i, j, pixels, mosaic_height, mosaic_width)
            pixels[i: i + mosaic_height, j: j + mosaic_width, :] = int(brightness // step_grad) * step_grad
            j = j + mosaic_width
        i = i + mosaic_height


pixels_img = np.array(Image.open('img2.jpg'))
size_h, size_w = 10, 10
num_grad = 50

make_mosaic(pixels_img, int(size_h), int(size_w), num_grad)

res = Image.fromarray(pixels_img)
res.save('res_filename.jpg')
