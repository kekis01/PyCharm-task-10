from PIL import Image
import numpy as np
import doctest


def find_brightness(i, j, pixels, m_h, m_w):
    """
    Высчитывает среднюю яркость серого цвета
    >>> find_brightness(10,10,np.array(Image.open("img2.jpg")),10,10)
    19.0
    >>> find_brightness(5,5,np.array(Image.open("img2.jpg")),5,5)
    17.0
    """
    count = np.sum(pixels[i: i + m_h, j: j + m_w]) / 3
    count = count // (m_h * m_w)
    return count


def make_mosaic(pixels, mosaic_height, mosaic_width, grad):
    """
    Обрабатывает данные для нового изображения, заданного размера, серого цвета
    """
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


if __name__ == '__main__':
    doctest.testmod()


images = input('Введите имя исходного файла и нового(через запятую): ').split(',')
pixels_img = np.array(Image.open(f"{images[0]}.jpg"))
size_h, size_w = input('Введите размер мозаики(через запятую): ').split(',')
num_grad = int(input('Введите число градации: '))

make_mosaic(pixels_img, int(size_h), int(size_w), num_grad)

res = Image.fromarray(pixels_img)
res.save(f"{images[1]}.jpg")
