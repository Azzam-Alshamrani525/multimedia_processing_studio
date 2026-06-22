import numpy as np
from PIL import Image

from processing.image_processing import clamp, pil_to_rgb_array, rgb_array_to_pil


def grayscale(image: Image.Image) -> Image.Image:
    pixels = pil_to_rgb_array(image)
    height, width, _ = pixels.shape
    result = np.zeros_like(pixels)

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[y, x]
            gray = clamp(0.299 * r + 0.587 * g + 0.114 * b)
            result[y, x] = [gray, gray, gray]

    return rgb_array_to_pil(result)


def sepia(image: Image.Image) -> Image.Image:
    pixels = pil_to_rgb_array(image)
    height, width, _ = pixels.shape
    result = np.zeros_like(pixels)

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[y, x]
            new_r = 0.393 * r + 0.769 * g + 0.189 * b
            new_g = 0.349 * r + 0.686 * g + 0.168 * b
            new_b = 0.272 * r + 0.534 * g + 0.131 * b
            result[y, x] = [clamp(new_r), clamp(new_g), clamp(new_b)]

    return rgb_array_to_pil(result)


def negative(image: Image.Image) -> Image.Image:
    pixels = pil_to_rgb_array(image)
    height, width, _ = pixels.shape
    result = np.zeros_like(pixels)

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[y, x]
            result[y, x] = [255 - r, 255 - g, 255 - b]

    return rgb_array_to_pil(result)


def posterization(image: Image.Image, levels: int = 4) -> Image.Image:
    levels = max(2, min(16, int(levels)))
    pixels = pil_to_rgb_array(image)
    height, width, _ = pixels.shape
    result = np.zeros_like(pixels)
    step = 256 // levels

    # Posterization is done by assigning every channel to the nearest reduced level.
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[y, x]
            result[y, x] = [
                clamp((int(r) // step) * step + step // 2),
                clamp((int(g) // step) * step + step // 2),
                clamp((int(b) // step) * step + step // 2),
            ]

    return rgb_array_to_pil(result)


COLOR_OPERATIONS = {
    "Grayscale": grayscale,
    "Sepia": sepia,
    "Negative": negative,
    "Posterization": posterization,
}
